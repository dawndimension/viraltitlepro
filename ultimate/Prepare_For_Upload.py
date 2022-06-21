#Prepare_For_Upload.py

from ast import Not
from cmath import nan
from operator import contains
import sys
import os
import random
import datetime
import time
import re
from time import strptime
from upload_video import *
import mimetypes

upload_limit = 6

def prepare_all(video_count, dir, titles_in_table, video_public_datetime):
    successful_prep_for_upload = False

    if not isinstance(video_count, int) or video_count < 1 or video_count > upload_limit:
        print("Video upload count is not valid: "+str(video_count))
        return False
        
    isValidDir = os.path.isdir(dir) 
    print(isValidDir)
    if not isValidDir:
        print("Not a valid directory, please enter a valid directory.")
        return False

    files_in_dir = get_files(dir)
    select_video_files_for_upload(files_in_dir,titles_in_table, video_count, dir)

    #validate timestamp
    valid_time = validate_timestamp(video_public_datetime)
    if valid_time != True:
         video_public_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


    return successful_prep_for_upload 


def select_video_files_for_upload(files_in_dir, titles_in_table, video_count, dir):
    #loop, at random based on video count, select videos that will be uploaded, 
    #create new map, with key = title, value = full path to filename
    # also call isVideo(files[index])  only attempt to upload video files
    return True


def get_files(staging_dir):       # 1.Get file names from directory  
    # Get list of all files in a given directory sorted by name
    file_list = sorted( filter( lambda x: os.path.isfile(os.path.join(staging_dir, x)),
                        os.listdir(staging_dir) ) )
    for file_name in file_list:
      print(file_name)
    
    return (file_list)

def validate_timestamp(video_public_datetime):
    # we want "%Y-%m-%d %H:%M"
    #Example: 2022-06-13 21:37

    try:
        datetime.datetime.strptime(video_public_datetime, '%Y-%m-%d %H:%M')
    except ValueError:
        print(video_public_datetime+' is Not a valid timestamp')
    else:
        print('You have supplied a valid date and time to schedule these videos...')
        return True

def isVideo(file):
    if mimetypes.guess_type('file_path')[0].startswith('video'):
        print('It is a video')
        return True
    else:
        print('It is not a video')
        return False
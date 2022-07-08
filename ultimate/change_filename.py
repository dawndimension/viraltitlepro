import os
import os.path
from pickle import FALSE, TRUE
import random
from Generate_Title import *
import glob
import shutil

# importing all the
# functions defined in test.py
#from test import *

#try https://pypi.org/project/grammar-check/ after generating the title to fix it.

#todo for each file in dir, run generate_title and rename file to that, then copy to upload folder. for now I will hard code a title name to return so it can work. later implement
#youtube api to upload. for me, python can always be running, and triggered when I drag files to that folder. drag files to folder, they get put in upload folder with names. then manually upload 
#them to youtube. when I design desktop app, people can drag files into app, or browse for them. it will work the same way though. use a temp folder then bring them to upload.
#later can upload them automatically. maybe have a preset scheduling options, and customizeable way. 1 a day at x. 1 every 15 minutes starting at x. max of 8? with api
#for now do everything in here, later organize

#test code
#os.chdir(r"title_staging")
#old_file_name = "new2.txt"
#new_file_name = "new2.txt"
#os.rename(old_file_name, new_file_name)
#print(old_file_name + " renamed to " + new_file_name);
# end test code



#can be a separate product from viral title pro. Will have it's own simple GUI and will be a free bonus software

video_count = 14
copy_from_dir="C:\\Users\\Brandon\\Desktop\\MINIGOLFUS\\exports\\_STAGING\\Viral_Title_Pro_Uploads"
#careful what you set upload dir as. Files are deleted from upload dir so DO NO set this to location where you store videos!!
upload_dir="C:\\Users\\Brandon\\Desktop\\MINIGOLFUS\\exports\\_STAGING\\experiment-616"
#upload_dir="D:\\carmanjaro\\renamer"
file_list = ""
subject = "putt putt video"
titles = []
tags = "#shorts #minigolf #golf"
file_extension = ".mp4"

def get_files(upload_dir):       # 1.Get file names from directory
    #file_list=os.listdir(upload_dir)
    #print ("Files in selected directory: "+str(file_list))
    
    # Get list of all files in a given directory sorted by name
    file_list = sorted( filter( lambda x: os.path.isfile(os.path.join(upload_dir, x)),
                        os.listdir(upload_dir) ) )
    for file_name in file_list:
      print(file_name)
    
    return (file_list)

def generate_filename_handler(subject,tags):
  new_title = generate_title(subject,tags)
  if "|" in new_title:
    new_title = new_title.replace("|", " - ")
  if "..." in new_title:
    new_title = new_title.replace("...", " - ")
  if "This World" in new_title:
    new_title = new_title.replace("This World", "The World")
  
  filename = new_title+" "+tags+file_extension
  print("New filename: "+filename)
  return filename


def rename_files_handler(files, upload_dir):
  os.chdir(upload_dir)

  print("Looping through current files in directory: "+upload_dir)
  for index, old_filename in enumerate(files):
    print (index, ",",old_filename)
    print("current filename:"+files[index])
        
    filename = generate_filename_handler(subject,tags)
    file_exists = os.path.exists(filename)

    while file_exists:
      print("File exists already, finding a different name...")
      filename = generate_filename_handler(subject,tags)
      file_exists = os.path.exists(filename)

    print("--")
    try:
      print("trying to rename files")
      os.rename(files[index], filename)   
        
    except FileExistsError:
      print("File already exists, trying different name...")
          
    except:
      print("An exception occurred")
      return False

    #iteration
    print("--------------")
  
  #End Loop
  print("Finished Changing Filenames for "+str(index+1)+" files")
  print ("DONE")
  return True
    

def delete_files_in_upload_dir(upload_dir):
  for f in os.listdir(upload_dir):
    os.remove(os.path.join(upload_dir, f))
  print("Files deleted from "+str(upload_dir))  

def copy_video_files_for_upload(files_in_dir, video_count, src_folder, dst_folder):
    #loop, at random based on video count, select videos that will be uploaded, 
    #copy files over to upload dir
    # also call isVideo(files[index])  only attempt to upload video files
    #shuffle list of files, grab last one, then discard it from list after use it using pop. this way no duplicates per upload.
    print("Listing files in source video folder before copy...")
    for x in range(video_count):
        print("files in dir before shuffle "+str(files_in_dir))
        random.shuffle(files_in_dir)
        print("files in dir after shuffle "+str(files_in_dir))
        
        # file names
        file = str(files_in_dir[-1])
        src_file = src_folder + "\\" + file
        dst_file = dst_folder + "\\" + file

        shutil.copyfile(src_file, dst_file)
        print('Copied')     
        
        files_in_dir.pop()
        print("files in dir after pop "+str(files_in_dir))
    print("===================")
    print("done copying files to upload directory...")

    return True



#optional - copy files randomly from videos directory into this directory
#delete files in upload dir before copying new ones over. the folder is a temporary one. 
#can also have it create a new folder with timestamp but that would use up space
delete_files_in_upload_dir(upload_dir)
files_in_dir = get_files(copy_from_dir)
Success = copy_video_files_for_upload(files_in_dir, video_count, copy_from_dir, upload_dir)

file_list = get_files(upload_dir)
Success = rename_files_handler(file_list, upload_dir)







#for file in os.listdir('title_staging'):
#    exit;




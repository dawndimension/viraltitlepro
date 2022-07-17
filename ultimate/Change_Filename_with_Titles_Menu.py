from ast import Not
from asyncio.windows_events import NULL
from pickle import FALSE, TRUE
from typing import List
import PySimpleGUI as sg
import subprocess

from pyparsing import Or, empty
from Generate_Title import *
from array import *
from datetime import datetime
from Prepare_For_Upload import *
import pyperclip as pc


#https://github.com/dawndimension/viraltitlepro
#F:/_PassiveFlows/Viral Title Pro/python/title_staging

#variables
title = None
video_count = 1
video_public_datetime = "2022-06-10 21:40:52"
date_picker_used = False
#make a single place to store all config later
video_max_limit = 15

#functions
def generate_title_loops(message, video_count):
    print(video_count)    
    return (generate_multiple_titles(message,"#shorts", video_count))

def copy2clip(txt):
    clip = pc.copy(txt)
    return clip




#### UI ####
sg.theme('SandyBeach')   # Add a touch of color
sg.theme_input_text_color('black')
headings = [" Num ", "Generated titles                                        ."]
titles_in_table = []


layout = [
            [sg.Text('Viral Clip Commando - Generate titles, change video filenames, and prep for drag and drop upload to Youtube.')],      
            [sg.Text('How Many Videos Will You Upload? - This is How Many Video Files Will Have Filename Changed to Generated Titles!',size=(100, 1), font='Lucida',justification='left')],
            [sg.Combo([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],default_value=1,key='_upload_count_',size=(30, 1))],
            [sg.Text('Enter your Video Subject',font='Lucida',justification='left')],
            [sg.Input(do_not_clear=True, enable_events=True, key='_IN_', size=(30,5))],
            [sg.Text('Enter your Tags(3)')],
            [sg.Input(do_not_clear=True, enable_events=True, key='_TAGS_', size=(30,5))],            
            [sg.Text("Choose Source directory: (folder that contains your video files that will be copied) ",font='Lucida',justification='left')],
            [sg.Input(), sg.FolderBrowse(key="-SRCDIR-")],
            [sg.Text("Choose temp directory: (this should be an EMPTY directory that videos will be copied to for upload)",font='Lucida',justification='left')],
            [sg.Input(), sg.FolderBrowse(key="-TEMPDIR-")],
            [sg.Button('Copy Video Files with Generated Titles'),sg.Button('Clear')],
         ]

# Create the Window
window = sg.Window('Main Menu', layout, resizable=True,finalize=True)
window.Maximize()
v=window.read()


while True:             # Event Loop
    event, values = window.Read()
    #print(event, values)
    if event is None or event == 'Exit':
        break


    if len(values['_IN_']) > 30:
        window.Element('_IN_').Update(values['_IN_'][:-1])
   


    #Generate title clicked
    if event == 'Copy Video Files with Generated Titles':
        print("Generate Title Clicked...")
        video_count = (values['_upload_count_'])
        
        if not str(video_count).isnumeric():
            print("value not numeric")
            video_count = 1
        
        if not isinstance(video_count, int):
            print("not an int. not doing anything here")
        
        if video_count == "":
            print("Desired count was empty")
            video_count = 1

        video_count = int(video_count)

        if video_count > video_max_limit:
            video_count = video_max_limit
        if video_count < 1:
            video_count = 1

        print ("Desired video count is "+str(video_count))
        srcdir = (values["-SRCDIR-"]) #directory selected will get saved in the database and used the next time program is opened.
        print("Dir is: "+str(srcdir)) 
        tempdir = (values["-TEMPDIR-"]) #directory selected will get saved in the database and used the next time program is opened.
        print("Dir is: "+str(tempdir)) 

window.Close()
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
video_max_limit = 6

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
            [sg.Text('Viral Title Ultimate - Generate titles and Upload videos all in one!')],      
            [sg.Text('How Many Videos Will You Upload?',size=(30, 1), font='Lucida',justification='left')],
            [sg.Combo([1,2,3,4,5,6],default_value=1,key='_upload_count_',size=(30, 1))],
            [sg.Text('Enter your Subject',font='Lucida',justification='left')],
            [sg.Input(do_not_clear=True, enable_events=True, key='_IN_', size=(30,5))],
            [sg.Text('Enter your Tags(3)')],
            [sg.Input(do_not_clear=True, enable_events=True, key='_TAGS_', size=(30,5))],            
            [sg.Text("Choose videos directory: ",font='Lucida',justification='left')],
            [sg.Input(), sg.FolderBrowse(key="-DIR-")],
            [sg.Button('Generate Title'),sg.Button('⧉'),sg.Button('Clear')],          
            [sg.Table(values=titles_in_table, headings=headings, justification='left', key='-TABLE-',col_widths = 105,def_col_width=105,max_col_width = 110, enable_events=True)],
            [sg.Button('Upload Videos', key = ('_UPLOAD_'), font=('Times New Roman',12),disabled=True),sg.Button('Exit', font=('Times New Roman',12)),
            [sg.Input(key='_DATE_', default_text="default=now",size=(20,1)), sg.CalendarButton('Schedule Videos', close_when_date_chosen=True,  target='_DATE_',format="%Y-%m-%d %H:%M",  enable_events=True, location=(40,40), no_titlebar=False, )],
            [sg.Text("Upload Interval: ",font='Lucida',justification='left')],
            [sg.Combo([15, 30 , 45, 60],default_value=15,key='_INTERVAL_',disabled=True,size=(15, 1)), sg.Text('minutes')]]
         ]

# Create the Window
window = sg.Window('Main Menu', layout, resizable=True,finalize=True)
window.Maximize()
v=window.read()

table = window['-TABLE-']

while True:             # Event Loop
    event, values = window.Read()
    #print(event, values)
    if event is None or event == 'Exit':
        break


    if len(values['_IN_']) > 30:
        window.Element('_IN_').Update(values['_IN_'][:-1])
   

    #while loop always checking if all fields are filled with valid values, 
    #in order for upload video btn to be enabled
    #while title != None and video_count > 0:

    if event == 'Date Picker':
        print ("test")

    #Generate title clicked
    if event == 'Generate Title':
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
        
        #reset field to corrected value
        window.Element('_upload_count_').update(video_count)

        title = generate_title_loops(values['_IN_'], video_count)       
        titles_in_table = []
        tags = (values['_TAGS_'])
        i = 0
        
        #tags present
        if tags != "":
            print("Going thru list of titles...")
            while i < len(title):
                print(title[i])            
                titles_in_table.append([i+1,title[i]+" "+tags])            
                i += 1        
            print("Here is output of data list after clicking generate title: ")
            print(titles_in_table)

        #tags not present (aka else)
        else:
            print("no tags supplied")
            while i < len(title):
                print("going thru list of titles - "+title[i])            
                titles_in_table.append([i+1,title[i]])            
                i += 1        
            print("here is output of data list after clicking generate title: ")
            print(titles_in_table)

        window.Element('-TABLE-').update(titles_in_table)
        window.Element('_UPLOAD_').update(disabled=False)  
        if len(titles_in_table) > 1:
            window.Element('_INTERVAL_').update(disabled=False)
        else:
            window.Element('_INTERVAL_').update(disabled=True)

    #copy title(s) to clipboard clicked
    
    if event == '⧉' and titles_in_table != []:
        title_string = "titles:"
        print("copying title(s)")  
            
        i = 0
        while i < len(title):
            print("going thru list - "+title[i])
            title_string += ''.join(title)
            i += 1            
            print (title_string)        
        copy2clip(title_string)
    
    #upload videos clicked
    if event == '_UPLOAD_':
        print ("=========Upload videos clicked===========")
        video_public_datetime = (values['_DATE_'])  #validate this in prepare_for_upload.py
        print("Selected date and time to upload videos: " +str(video_public_datetime))
        #make separate class Upload_Validation.py - ensure all fields valid values. default timestamp if empty is now
        dir = (values["-DIR-"]) #directory selected will get saved in the database and used the next time program is opened.
        print("Dir is: "+str(dir))
        upload_interval = (values["_INTERVAL_"]) #save this in db too, default 15, so dont have to touch
        print("Selected upload interval for vidoes: "+str(upload_interval))

        #call prepare_all to initiate video selection
        #video count, video directory, titles, timestamp(convert to epoch, then back later), interval
        #instead of passing in video_count from how many videos upload dropdown, lets just count titles generated and use that.
        successful_prep_for_upload = prepare_all(dir, titles_in_table, video_public_datetime)
        print ("Video successfully prepared for upload?: "+str(successful_prep_for_upload)+ ".")

    #clear titles from table
    if event == ('Clear'):
        print("deleting titles")
        titles_in_table = []
        title = []
        window.Element('-TABLE-').update(titles_in_table)
            

window.Close()
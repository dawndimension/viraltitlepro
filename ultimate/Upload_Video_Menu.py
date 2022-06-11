from typing import List
import PySimpleGUI as sg
import subprocess
from Generate_Title import *
from array import *

#https://github.com/dawndimension/viraltitlepro
#variables
title = None
video_count = 0
video_public_datetime = "2022-06-10 21:40:52"


#functions
def generate_title_loops(message, video_count):
    print(video_count)    
    return (generate_multiple_titles(message,"#shorts", video_count))

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)


  



#### UI ####
sg.theme('SandyBeach')   # Add a touch of color
sg.theme_input_text_color('black')
headings = [" Num ", "Generated titles                                        ."]
data = []


layout = [
            [sg.Text('Viral Title Ultimate - Generate titles and Upload videos all in one!')],      
            [sg.Text('How Many Videos Will You Upload?',size=(30, 1), font='Lucida',justification='left')],
            [sg.Combo([1,2,3,4,5,6],default_value=1,key='_upload_count_',size=(30, 1))],
            [sg.Text('Enter your Subject',font='Lucida',justification='left')],
            [sg.Input(do_not_clear=True, enable_events=True, key='_IN_', size=(30,5))],
            [sg.Button('Generate Title'),sg.Button('⧉'),sg.Button('Clear')],          
            [sg.Table(values=data, headings=headings, justification='left', key='-TABLE-',col_widths = 105,def_col_width=105,max_col_width = 110, enable_events=True)],
            #[sg.Multiline('--Generated Titles--',size=(100,7), key='_OUT_')],
            [sg.Button('Upload Video(s)', font=('Times New Roman',12),disabled=True),sg.Button('Exit', font=('Times New Roman',12)),
            [sg.Input(default_text="NOW",key='_DATE_', size=(20,1)), sg.CalendarButton('Date Picker', close_when_date_chosen=True,  target='_DATE_', location=(40,40), no_titlebar=False, )]]
         ]

# Create the Window
window = sg.Window('Main Menu', layout, resizable=True,finalize=True)
window.Maximize()
v=window.read()

table = window['-TABLE-']

while True:             # Event Loop
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break
    if len(values['_IN_']) > 30:
        window.Element('_IN_').Update(values['_IN_'][:-1])
    
    #while title != None and video_count > 0:
        

    if event == 'Generate Title':
        video_count = (values['_upload_count_'])
        title = generate_title_loops(values['_IN_'], video_count)      
        #window.Element('_OUT_').update(title)
        
        data = []
        #data.append(['aa1', 'aa2'])

        i = 0
        while i < len(title):
            print("going thru list - "+title[i])
            #item = title[i].replace(" ", " ")
            #data.append(i,item)
            data.append([i+1,title[i]])
            #window.Element('-TABLE-').update(data)
            i += 1
        
        
        print("here is output of data list after clicking generate title: ")
        print(data)    

        #data = title
        window.Element('-TABLE-').update(data)         
    
    if event == '⧉':
        if event == '⧉':
            title_string = "titles:"
            print(data)
            print(title)
            
        i = 0
        while i < len(title):
            print("going thru list - "+title[i])
            title_string += ''.join(title)
            i += 1            
            print (title_string)
        
        copy2clip(title_string)
    
    
    if event == "Upload Video(s)":
        video_count = (values['_upload_count_'])
        print(video_count)
        video_public_datetime = (values['_DATE_'])
        print(video_public_datetime)
    
    #table
    if event == ('Clear'):
        data = []
        window.Element('-TABLE-').update(data)
            

window.Close()
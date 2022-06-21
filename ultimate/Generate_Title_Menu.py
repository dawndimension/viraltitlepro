#Generate_Title_Menu.py
#this is a simple UI exclusively for title generation. 
#Will likely be a free bonus product

import PySimpleGUI as sg
import subprocess
from Generate_Title import *
import pyperclip as pc

sg.theme('BlueMono')   # Add a touch of color
sg.theme_input_text_color('black')

def generate_title_placeholder(message):
    return (generate_title(message,"#shorts"))

def copy2clip(txt):
    clip = pc.copy(txt)
    # old way cmd='echo '+txt.strip()+'|clip'
    #return subprocess.check_call(cmd, shell=True)
    return clip
    
layout = [
            [sg.Text('Viral Title Generator')],      
            [sg.Text('Enter your Subject')],
            [sg.Input(do_not_clear=True, enable_events=True, key='_IN_', size=(50,5))],
            [sg.Text('Enter your Tags(3)')],
            [sg.Input(do_not_clear=True, enable_events=True, key='_TAGS_', size=(30,5))],
            [sg.Button('Generate'),sg.Button('Exit')],
            [sg.Input('--Generated Title--',size=(50,5), key='_OUT_')],
            [sg.Button('⧉')],
         ]

# Create the Window
window = sg.Window('Main Menu', layout,default_element_size=(12, 1), resizable=True,finalize=True)
window.Maximize()

while True:             # Event Loop
    event, values = window.Read()
    #print(event, values)
    if event is None or event == 'Exit':
        break
    if len(values['_IN_']) > 30:
        window.Element('_IN_').Update(values['_IN_'][:-1])
    
    if event == 'Generate':
        title = generate_title_placeholder(values['_IN_'])        
        tags = (values['_TAGS_'])
        print (tags)
        window.Element('_OUT_').update("x")
        window.Element('_OUT_').update(title+" "+tags)
    if event == '⧉':
        copy2clip(str(values['_OUT_']))
window.Close()
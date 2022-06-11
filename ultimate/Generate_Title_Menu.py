import PySimpleGUI as sg
import subprocess
from Generate_Title import *


sg.theme('BlueMono')   # Add a touch of color
sg.theme_input_text_color('black')

def generate_title_placeholder(message):
    return (generate_title(message,"#shorts"))

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

layout = [
            [sg.Text('Viral Title Generator')],      
            [sg.Text('Enter your Subject')],
            [sg.Input(do_not_clear=True, enable_events=True, key='_IN_', size=(35,5))],
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
        window.Element('_OUT_').update("x")
        window.Element('_OUT_').update(title)
    if event == '⧉':
        copy2clip(values['_OUT_'])
window.Close()
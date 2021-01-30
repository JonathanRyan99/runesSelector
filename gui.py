
import PySimpleGUI as sg
import main
import sys
import os
from pathlib import Path


sg.theme("lightGrey")

#pyinstaller changes the cwd() when compiled so have to do this to get back to the local folder
basedir = os.path.dirname(sys.executable)
baseDirPath = Path(basedir)
saveDirectoryPath = baseDirPath/"saves"


files = os.listdir(saveDirectoryPath)
choices = []
for name in files:
       extension = name.split(".")
       choices.append(extension[0])



layout = [  [sg.Text('Enter a MobaFire Link')],
            [sg.Text('MobaFire link', size=(15, 1)), sg.InputText(key='-USERLINK-'), sg.Button('Build')],
            [sg.Text('Save as ', size=(15, 1)), sg.InputText(key='-SAVENAME-') , sg.Button('Save'), ],
            [sg.Text('Pick from your saved builds')],
            [sg.Listbox(choices, size=(15, len(choices)), key='-CHAMP-'), sg.Output(size=(50,10), key='-OUTPUT-')],
            [sg.Button('Ok')]  ]

window = sg.Window('RuneSelector', layout)

while True:    # the event loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Ok':
        if values['-CHAMP-']:    # if something is highlighted in the list
            
            name = str(values['-CHAMP-'])
            name = name[2:]
            name = name[:(len(name)-2)]
            print("Loading build: ", name)
            main.readfile(name ,saveDirectoryPath)

    if event == 'Build':
        if values['-USERLINK-']:
            userRunes = main.scrapRunes(values['-USERLINK-'])
            main.RuneBuilder(userRunes)

    if event == 'Save':
        if values['-USERLINK-'] and values['-SAVENAME-']:
            main.saveFile(values['-SAVENAME-'],values['-USERLINK-'],saveDirectoryPath)
            sg.popup(f"RunePage saved:  {values['-SAVENAME-']} \n new entry visiable on restart")


window.close()


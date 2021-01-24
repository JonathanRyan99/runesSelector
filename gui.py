
import PySimpleGUI as sg
import main
import os
from pathlib import Path


sg.theme("lightGrey")

path = Path(__file__).parent/"saves"
files = os.listdir(path)
choices = []
for name in files:
       extension = name.split(".")
       choices.append(extension[0])



layout = [  [sg.Text('Enter a MobaFire Link')],
            [sg.Text('MobaFire link', size=(15, 1)), sg.InputText(key='-USERLINK-'), sg.Button('Build')],
            [sg.Text('Save as ', size=(15, 1)), sg.InputText(key='-SAVENAME-') , sg.Button('Save'), ],
            [sg.Text('Pick from your saved builds')],
            [sg.Listbox(choices, size=(15, len(choices)), key='-CHAMP-')],
            [sg.Button('Ok')]  ]

window = sg.Window('RuneSelector', layout)

while True:    # the event loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Ok':
        if values['-CHAMP-']:    # if something is highlighted in the list
            
            name = str(values['-CHAMP-'])
            print(name)
            name = name[2:]
            print(name)
            name = name[:(len(name)-2)]
            print(name)
            main.readfile(name)

    if event == 'Build':
        if values['-USERLINK-']:
            userRunes = main.scrapRunes(values['-USERLINK-'])
            main.RuneBuilder(userRunes)

    if event == 'Save':
        if values['-USERLINK-'] and values['-SAVENAME-']:
            main.saveFile(values['-SAVENAME-'],values['-USERLINK-'])
            sg.popup(f"RunePage saved:  {values['-SAVENAME-']}")


window.close()


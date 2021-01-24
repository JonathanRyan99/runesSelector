
import PySimpleGUI as sg
import main

sg.theme("lightGrey")
choices = ["poppy","jinx","garen","bard"]


layout = [  [sg.Text('Enter a MobaFire Link')],
            [sg.Text('MobaFire link', size=(15, 1)), sg.InputText(key='userLink'), sg.Button('Build')],
            [sg.Text('Save as ', size=(15, 1)), sg.InputText(key='saveName') , sg.Button('save'), ],
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
            sg.popup(f"build selected: {values['-CHAMP-'][0]}")
window.close()


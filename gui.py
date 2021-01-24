
import PySimpleGUI as sg
import main

sg.theme("lightGrey")
choices = ["poppy","jinx","garen","bard"]


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
            sg.popup(f"selected: {values['-CHAMP-']}")

    if event == 'Build':
        if values['-USERLINK-']:
            userRunes = main.scrapRunes(values['-USERLINK-'])
            main.RuneBuilder(userRunes)

    if event == 'Save':
        if values['-USERLINK-'] and values['-SAVENAME-']:
            main.saveFile(values['-SAVENAME-'],values['-USERLINK-'])
            sg.popup(f"RunePage saved:  {values['-SAVENAME-']}")


window.close()


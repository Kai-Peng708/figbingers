import PySimpleGUI as pyg

pyg.theme('DarkAmber')
# Stuff inside your window

layout = [[pyg.Text('Text Entry:'), pyg.Text(size=(100, 1), key='-OUTPUT-')],
          [pyg.Text('Word Count:'), pyg.Text(size=(3,1), key='-WORDCOUNT-')],
          [pyg.Input(key='-IN-')],
          [pyg.Button('Count'), pyg.Button('Exit')]]

window = pyg.Window('Display', layout)

while True:
    event, values = window.read()
    print(event, values)
    window['-OUTPUT-'].update(values['-IN-'])
    if event == pyg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Count':
        window['-WORDCOUNT-'].update(len(values['-IN-'].split()))
        # window['-OUTPUT-'].update(values['-IN-'])

window.close()



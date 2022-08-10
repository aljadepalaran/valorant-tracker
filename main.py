import PySimpleGUI as sg


def main():
    layout = [[sg.Text("Name"), sg.Input(key='-NAME-')],
              [sg.Text("Tag"), sg.Input(key='-TAG-')],
              [sg.Button('Load', pad=(250,50))],
              [sg.Text(size=(40, 1), key='-OUTPUT-')]]

    window = sg.Window('Valorant Tracker', layout)

    while True:
        event, values = window.read()

        if event == 'Load':
            print('You clicked load.')
            run_command()
        elif event == sg.WINDOW_CLOSED:
            break
        window['-TAG-'].update('Name: ' + values['-NAME-'] + "! Thanks for trying PySimpleGUI")

        # window['-TAG-'] refers to component with key='-TAG-'

    window.close()


def run_command():
    print('Hello World!')


main()

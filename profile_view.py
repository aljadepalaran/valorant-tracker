import PySimpleGUI as sg


def profile_view():
    return [[sg.Text("Name"), sg.Input(key='-NAME-')],
              [sg.Text("Tag"), sg.Input(key='-TAG-')],
              [sg.Multiline(default_text="Awaiting input.", key='-MULTI-', size=(50, 10)),sg.Image(key='-SMALL-')],
              [sg.Image(key='-WIDE-')],
              [sg.Image(key='-LARGE-')],
              [sg.Button('Load', pad=(250, 50))],
              [sg.Text(size=(40, 1), key='-OUTPUT-')]]

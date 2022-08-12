import PySimpleGUI as sg


def profile_view():
    return [[sg.Multiline(default_text="Awaiting input.", key='-MULTI-', size=(50, 10)),sg.Image(key='-SMALL-')],
              [sg.Image(key='-WIDE-')],
              [sg.Image(key='-LARGE-')],
              [sg.Text(size=(40, 1), key='-OUTPUT-')]]

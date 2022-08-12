import PySimpleGUI as sg


def profile_view():
    return [[sg.Multiline(default_text="Awaiting input.",
                          key='-PROFILE_MULTI-', size=(100, 10)),sg.Image(key='-PROFILE_SMALL-')],
            [sg.Image(key='-PROFILE_WIDE-')],
            [sg.Image(key='-PROFILE_LARGE-')],
            [sg.Text(size=(40, 1), key='-PROFILE_OUTPUT-')]]

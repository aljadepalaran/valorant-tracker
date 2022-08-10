import PySimpleGUI as sg
import requests as rq
import json
import time


def main():
    layout = [[sg.Text("Name"), sg.Input(key='-NAME-')],
              [sg.Text("Tag"), sg.Input(key='-TAG-')],
              [sg.Multiline(default_text="Awaiting input.", key='-MULTI-', size=(50, 10))],
              [sg.Button('Load', pad=(250, 50))],
              [sg.Text(size=(40, 1), key='-OUTPUT-')]]

    window = sg.Window('Valorant Tracker', layout)

    def get_user_information(_name, _tagline):  # requests the information from the website with appropriate name/tag
        try:
            request_url = f"https://api.henrikdev.xyz/valorant/v1/account/{_name}/{_tagline}"
            time_then = time.time()
            user_data = rq.get(request_url, timeout=1)
            time_now = time.time()
            print(f"Time taken for request= {round(time_now-time_then, 2)}s.")
            print(f"GET {request_url}")

            if user_data.ok:
                text, images = parse_data(user_data)  # yields the information text and a list of the image links
                window['-MULTI-'].update(text)  # updates the text in the multiline to the information requested
            else:
                print(f"User not found. Error Code: {user_data.status_code}")
                sg.Popup(f"User {_name} with tagline {_tagline} not found. Error Code: {user_data.status_code}.")

        except rq.exceptions.ReadTimeout:  # has the connection timed out?
            print('Connection timed out.')
            sg.Popup("Connection timed out.")  # inform user the connection timed out
    while True:
        event, values = window.read()

        if event == 'Load':
            get_user_information(values['-NAME-'], values['-TAG-'])  # check the boxes for information
        elif event == sg.WINDOW_CLOSED:
            break

        # window['-TAG-'] refers to component with key='-TAG-'

    window.close()


def parse_data(user_data):  # reformat the received data and return a large text string, and image links to display
    parsed_data = json.loads(user_data.content)
    image_links = []
    big_text = ''
    for key in parsed_data['data']:
        if key == 'card':
            image_links.append(parsed_data['data'][key]['small'])
            image_links.append(parsed_data['data'][key]['large'])
            image_links.append(parsed_data['data'][key]['wide'])
            continue
        else:
            big_text += f"{key.capitalize()}: {parsed_data['data'][key]}\n"
    return big_text, image_links


main()

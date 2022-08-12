import PySimpleGUI as sg
import requests as rq
import time
from models.user import User
from profile_view import profile_view
from matches import matches_view

layout_three = [[sg.Text('Hello world 3')]]

tab_group = [
    [[sg.Text("Name"), sg.Input(key='-NAME-')],
     [sg.Text("Tag"), sg.Input(key='-TAG-')],
     sg.TabGroup(
         [
             [
                 sg.Tab('Profile View', profile_view(), background_color='green'),
                 sg.Tab('Matches', matches_view(), background_color='blue'),
                 sg.Tab('Layout 3', layout_three, background_color='pink')
             ]
         ]
     ),
     sg.Button('Exit')
     ]
]

window = sg.Window('Test', tab_group)


def get_user_from_database(name_, tag_):
    try:
        return User.get(User.name == name_ and User.tag == tag_)
    except:
        print("Unable to retrieve user from the database.")
        return None


def fetch_user_data_from_api(name_, tag_):
    request_url = f"https://api.henrikdev.xyz/valorant/v1/account/{name_}/{tag_}"
    print(f"GET {request_url}")
    try:
        time_then = time.time()
        user_data = rq.get(request_url, timeout=1)
        time_now = time.time()
        print(f"Time taken for request= {round(time_now - time_then, 2)}s.")
        return user_data
    except rq.exceptions.ReadTimeout:  # has the connection timed out?
        print('Connection timed out.')
        sg.Popup("Connection timed out.")  # inform user the connection timed out
    return None


def check_puuid(user_puuid):
    if User.get(User.puuid == user_puuid) is None:
        return False
    else:
        return True


def update_user(user):
    return None


def display_data():
    return None


def add_user_to_database(user):
    return None


while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WINDOW_CLOSED:
        break
    elif event == 'Search':
        username = values['-NAME-']
        usertag = values['-TAG-']
        user = get_user_from_database()  # attempt to retrieve user from database
        if user is None:  # if user not in database, get from API
            user_api = fetch_user_data_from_api(username, usertag)
            if check_puuid(user_api):  # check if puuid already exists in database
                update_user(user_api)
                display_data()
            else:
                add_user_to_database(user)
        else:
            should_update = User.should_update_from_api()
            if should_update:
                user = fetch_user_data_from_api()
                update_user(user)
            display_data()

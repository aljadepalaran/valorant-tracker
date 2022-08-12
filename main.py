import PySimpleGUI as sg
import requests as rq
import time
import json
import Debug

from peewee import *
from models.user import User
from profile_view import profile_view
from matches import matches_view
sg.theme('Dark')
layout_three = [[sg.Text('Hello world 3')]]

tab_group = [
    [[sg.Text("Name"), sg.Input(key='-NAME-')],
     [sg.Text("Tag"), sg.Input(key='-TAG-')],
     [sg.Button('Search', pad=(250, 50))],
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
    Debug.log(f"#get_user_from_database, name:{name_}, tag:{tag_}")
    try:
        return User.get(User.name == name_ and User.tag == tag_)
    except:
        Debug.log("Unable to retrieve user from the database.")
        return None


def fetch_user_data_from_api(name_, tag_):
    Debug.log(f"#fetch_user_data_from_api, name:{name_}, tag:{tag_}")
    request_url = f"https://api.henrikdev.xyz/valorant/v1/account/{name_}/{tag_}"
    Debug.log(f"(HTTP Request)GET {request_url}")
    try:
        time_then = time.time()
        user_data = rq.get(request_url, timeout=1)
        time_now = time.time()
        Debug.log(f"Time taken for request= {round(time_now - time_then, 2)}s.")
        return user_data
    except rq.exceptions.ReadTimeout:  # has the connection timed out?
        Debug.log('Connection timed out.')
        sg.Popup("Connection timed out.")  # inform user the connection timed out
    return None


def check_puuid(parsed_user_data_):
    Debug.log(f"#check_puuid, data:{parsed_user_data_}")
    try:
        User.get(User.puuid == parsed_user_data_['puuid'])
        Debug.log("#check_puuid User already exists")
        return True
    except:
        return False


def update_user(parsed_user_data_):
    Debug.log(f"#update_user, data: {parsed_user_data_}")
    try:
        # set the updated values
        user_from_puuid = User.get(User.puuid == parsed_user_data_['puuid'])
        user_from_puuid.region = parsed_user_data_['region']
        user_from_puuid.account_level = parsed_user_data_['account_level']
        user_from_puuid.image_small_url = parsed_user_data_['card']['small']
        user_from_puuid.image_large_url = parsed_user_data_['card']['large']
        user_from_puuid.image_wide_url = parsed_user_data_['card']['wide']
        user_from_puuid.name = parsed_user_data_['name']
        user_from_puuid.tag = parsed_user_data_['tag']

        user_from_puuid.save()  # save the user
        Debug.log(f"#update_user, User update successfully")
    except:
        Debug.log("Could not update the user")


def display_data(databaseuser):
    Debug.log(f"#display_data{databaseuser}")
    some_text = f"""
        Puuid: {databaseuser.puuid}
        Region: {databaseuser.region}
        Name: {databaseuser.name}
        Tag: {databaseuser.tag}
        Account level: {databaseuser.account_level}
        Image Small: {databaseuser.image_small_url}
        Image Large: {databaseuser.image_large_url}
        Image Wide: {databaseuser.image_wide_url}
        Time of last update: {time.ctime(databaseuser.time_last_updated_unix)}
        """
    window['-PROFILE_MULTI-'].update(some_text)


def add_user_to_database(parsed_user_data_):
    try:
        User.create(puuid=parsed_user_data_['puuid'],
                    region=parsed_user_data_['region'],
                    account_level=parsed_user_data_['account_level'],
                    image_small_url=parsed_user_data_['card']['small'],
                    image_large_url=parsed_user_data_['card']['large'],
                    image_wide_url=parsed_user_data_['card']['wide'],
                    name=parsed_user_data_['name'],
                    tag=parsed_user_data_['tag'],
                    time_last_updated_unix=time.time())
        Debug.log(f"#added user to database {parsed_user_data_}")
    except IntegrityError:  # this error indicates the username is already in the database
        Debug.log('Username has already been used.')


def parse_user_api_data(user_api_data_):
    parsed_data = json.loads(user_api_data_.content)['data']
    Debug.log(f"#parse_user_api_data | {parsed_data}")
    return parsed_data


while True:
    event, values = window.read()

    if event == 'Exit' or event == sg.WINDOW_CLOSED:
        break

    elif event == 'Search':
        username = values['-NAME-']
        usertag = values['-TAG-']
        user = get_user_from_database(username, usertag)  # attempt to retrieve user from database

        if user is None:  # if user not in database, get from API
            user_api_data = fetch_user_data_from_api(username, usertag)
            parsed_user_data = parse_user_api_data(user_api_data)

            if check_puuid(parsed_user_data):  # check if puuid already exists in database
                update_user(parsed_user_data)
                user = get_user_from_database(username, usertag)
                print("here1")
                Debug.log(f"#updating the user info {user}")
                display_data(user)

            else:
                add_user_to_database(parsed_user_data)
                user = get_user_from_database(username, usertag)
                display_data(user)

        else:
            should_update = user.should_update_from_api()

            if should_update:
                user_api_data = fetch_user_data_from_api(username, usertag)
                parsed_user_data = parse_user_api_data(user_api_data)
                update_user(parsed_user_data)

            display_data(user)
            print("here2")

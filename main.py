import PySimpleGUI as sg
from profile_view import profile_view
from matches import matches_view

layout_three = [[sg.Text('Hello world 3')]]

tab_group = [
    [
        sg.TabGroup(
            [
                [
                    sg.Tab('Profile View', profile_view(), background_color='green'),
                    sg.Tab('Matches', matches_view(), background_color='blue'),
                    sg.Tab('Layout 3', layout_three, background_color='pink'),
                    sg.Button('Exit')
                ]
            ]
        )
    ]
]

window = sg.Window('Test', tab_group)

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WINDOW_CLOSED:
        break
    elif event == 'Search':
        user = get_user_from_database()
        if user == None:
            user = fetch_user_data_from_api()
            if check_puuid():  # if puuid exists in database / user updated
                update_user(user)
                display_data()
            else:
                add_user_to_database(user)
        else:
            should_update = User.should_update_from_api()
            if should_update:
                user = fetch_user_data_from_api()
                update_user(user)
            display_data()


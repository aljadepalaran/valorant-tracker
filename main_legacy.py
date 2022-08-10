import requests as rq
import json
from tkinter import *
from tkinter import ttk
import numpy as np
import PySimpleGUI as sg

# this defines the window for tkinter
root = Tk()
# get the screen width and height of the user's window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# window scaling factor compared to the users screen
size_scale = .5
# make window with the scaled size
root.geometry(f"{int(screen_width * size_scale)}x{int(screen_height * size_scale)}")
root.configure(background='grey')


def draw_interface():  # create labels and entries
    Label(root, text='Name').place(x=0, y=0, height=20, width=50)  # name label and entry box
    name_entry = Entry(root, width=20)
    name_entry.place(x=75, y=0, height=20)

    Label(root, text='Tag').place(x=0, y=30, height=20, width=50)  # tag label and entry box
    tag_entry = Entry(root, width=20)
    tag_entry.place(x=75, y=30, height=20)

    Label(root, text='Status').place(x=0, y=60, height=20, width=50)  # status label and entry box
    status_entry = Entry(root, width=20, state='disabled')
    status_entry.place(x=75, y=60, height=20)

    def button_command():  # load button command
        ttk.Label(root, text=f"test").pack()
        get_user_information(name_entry.get(), tag_entry.get())

    def update_status(error_code):  # updates the box with the status error from getting the information
        status_entry.configure(state='normal')
        status_entry.insert('end', error_code)
        status_entry.configure(state='disabled')

    def get_user_information(_name, _tagline):  # requests the information from the website with appropriate name/tag
        try:
            request_url = f"https://api.henrikdev.xyz/valorant/v1/account/{_name}/{_tagline}"
            user_data = rq.get(request_url, timeout=1)

            print(f"GET {request_url}")

            if user_data.ok:
                parse_data(user_data)
            else:
                print(f"User not found. Error Code: {user_data.status_code}")
                update_status(user_data.status_code)

        except rq.exceptions.ReadTimeout:
            print('Connection timed out.')

    ttk.Button(root, text="Load", command=button_command).pack()


def clear_interface():  # wipes the entire window
    for widget in root.winfo_children():
        widget.destroy()

    root.pack_forget()


def refresh_data():
    clear_interface()
    draw_interface()


def parse_data(user_data):  # reformats the received data and displays to the user
    count = 0  # used to change the row in which the text is placed
    parsed_data = json.loads(user_data.content)
    for key in parsed_data['data']:

        if key == 'card':
            # ttk.Label(root, text="Profile Picture:").pack()
            # ttk.Label(root, text="Profile Picture:").pack()
            # ttk.Label(frm, text=f"Profile Picture:").grid(column=0, row=count)
            # ttk.Label(frm, text=f"{parsed_data['data'][key]['small']}").grid(column=1, row=count)
            # count += 1

            # ttk.Label(root, text="Profile Picture:").pack()
            # ttk.Label(root, text="Profile Picture:").pack()
            # ttk.Label(frm, text=f"Banner:").grid(column=0, row=count)
            # ttk.Label(frm, text=f"{parsed_data['data'][key]['large']}").grid(column=1, row=count)
            # count += 1

            # ttk.Label(root, text="Profile Picture:").pack()
            # ttk.Label(root, text="Profile Picture:").pack()
            # ttk.Label(frm, text=f"In-game Banner:").grid(column=0, row=count)
            # ttk.Label(frm, text=f"{parsed_data['data'][key]['wide']}").grid(column=1, row=count)
            continue
        else:
            ttk.Label(root, text=f"{key.capitalize()}: {parsed_data['data'][key]}").pack()
        count += 1


draw_interface()  # have to draw the interface for the first time
root.mainloop()

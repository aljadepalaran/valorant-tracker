import PySimpleGUI as sg
import requests as rq
import time
import json
import Debug

from peewee import *
from models.user import User
from profile_view import profile_view
from matches import matches_view


def fetch_last_5_matches(name_, tag_):
    request_url = f"https://api.henrikdev.xyz/valorant/v3/matches/eu/{name_}/{tag_}?filter=competitive"
    Debug.log(f"#fetch_last_5_matches {request_url}")
    try:
        time_then = time.time()
        match_data = rq.get(request_url, timeout=10)
        time_now = time.time()
        Debug.log(f"Time taken for request= {round(time_now - time_then, 2)}s.")
        Debug.log(f"#match_data {match_data}")
        return match_data
    except rq.exceptions.ReadTimeout:  # has the connection timed out?
        Debug.log('Connection timed out.')
        sg.Popup("Connection timed out.")  # inform user the connection timed out

def parse_match_data(match_data_):
    parsed_match_data = json.loads(match_data_.content)['data']
    Debug.log(f"# parse match data {parsed_match_data}")

somematchdata = fetch_last_5_matches("c00k1e","8878")
parse_match_data(somematchdata)
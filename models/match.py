from peewee import *
import time
import Debug

db = SqliteDatabase("main.db")


class Match(Model):
    class Metadata(Model):
        "map" = "Breeze",
        "game_version" = "release-05.00-shipping-11-729462",
        "game_length" = 1851221,
        "game_start" = 1657136764,
        "game_start_patched" = "Wednesday, July 6, 2022 9=46PM",
        "rounds_played" = 20,
        "mode" = "Competitive",
        "queue" = "Standard",
        "season_id" = "67e373c7-48f7-b422-641b-079ace30b427",
        "platform" = "PC",
        "matchid" = "4364fa0c-4419-4c1b-bb8f-12d1356c15cc",
        "region" = "eu",
        "cluster" = "London"

    class Players(Model):
        class All_Players(Model):
            puuid
            name
            tag
            team
            level
            character
            currenttier
            currenttier_patched
            player_card
            player_title
            party_id

            class Session_Playtime(Model):
                minutes
                seconds
                milliseconds

            class Behaviour(Model):
                afk_rounds
                class Friendly_Fire(Model):
                    incoming
                    outgoing
                rounds_in_spawn

            class Platform(Model):
                type
                class os(Model)
                    name
                    version
            class Ability_Casts(Model):
                c_cast
                q_cast
                e_cast
                x_cast
            class Assets(Model):
                class Card(Model):
                    'small': 'https://media.valorant-api.com/playercards/546c9535-4671-e7cf-d5f9-1b90e3e2d7e4/smallart.png',
                    'large': 'https://media.valorant-api.com/playercards/546c9535-4671-e7cf-d5f9-1b90e3e2d7e4/largeart.png',
                    'wide': 'https://media.valorant-api.com/playercards/546c9535-4671-e7cf-d5f9-1b90e3e2d7e4/wideart.png'
                class Agent(Model):
                    'small': 'https://media.valorant-api.com/agents/320b2a48-4d9b-a075-30f1-1f93a9b638fa/displayicon.png',
                    'bust': 'https://media.valorant-api.com/agents/320b2a48-4d9b-a075-30f1-1f93a9b638fa/bustportrait.png',
                    'full': 'https://media.valorant-api.com/agents/320b2a48-4d9b-a075-30f1-1f93a9b638fa/fullportrait.png',
                    'killfeed': 'https://media.valorant-api.com/agents/320b2a48-4d9b-a075-30f1-1f93a9b638fa/killfeedportrait.png'
            class Stats(Model):
                score
                kills
                deaths
                assists
                bodyshots
                headshots
                legshots
            class Economy(Model):
                class spent():
                    overall
                    average
                class loadout_value:
                    overall
                    average
            damage_made
            damage_received
        class Red(Model):
            array()
        class Blue(Model):
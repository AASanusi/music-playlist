"""
Import APIs and colorama library
"""

import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('weekly_playlist')


def weekly_playlist_welcome():
    """
    Introducing and informing the user about
    the application.
    """
    print(Back.YELLOW + Fore.BLUE + 'Welcome music lovers!\n')
    print(Back.YELLOW + Fore.BLUE + 'This is the weekly music playlist!\n')
    print(Fore.GREEN + Style.BRIGHT + 'Listening to music is life.')
    print(Fore.GREEN + Style.BRIGHT + 'Use this playlist to check out songs')
    print(Fore.GREEN + Style.BRIGHT + 'and add your own songs to any week.\n')

    print("Enter '1' to choose which week's playlist you would")
    print("like to view.\n")
    print("Enter '2' to choose which week's playlist you would")
    print("like to add songs to.\n")


def view_or_add():
    """
    The route the user takes to either view songs from the playlist or
    add songs to the playlist.
    """
    route = input("Please choose either (1 to view) or (2 to add)\n")
    if route == '1':
        view_playlist()
    elif route == '2':
        add_songs()
    else:
        print("Entry incorrect. Need to enter 1 or 2\n")
        return view_or_add()


def view_playlist():
    """
    This function will reveal each of the week's playlist they can choose from
    """
    print("\n Choose which week's playlist you would like to view")
    print("Please choose one of the week's number: '1' '2' '3' '4'\n")

    choice = input("Enter (1) or (2) or (3) or (4) to choose week playlist\n")

    if choice == "1":
        playlist_songs('week_one')
    elif choice == "2":
        playlist_songs('week_two')
    elif choice == "3":
        playlist_songs('week_three')
    elif choice == "4":
        playlist_songs('week_four')
    else:
        

def main():
    """
    Main function is used to run the program
    """
    weekly_playlist_welcome()


main()

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


def main():
    """
    Main function is used to run the program
    """
    weekly_playlist_welcome()


main()

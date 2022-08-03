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
    print(Back.YELLOW + 'Welcome music lovers to the weekly music playlist!\n')
    print(Fore.GREEN + 'Finding and listening to music is life.')
    print(Fore.GREEN + 'Use this playlist to check out songs for each week')
    print(Fore.GREEN + Style.BRIGHT + 'and add your own songs to any week.')



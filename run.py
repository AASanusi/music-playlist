"""
Import APIs and colorama library
"""
import sys
from tabulate import tabulate
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

    print(Fore.CYAN + "Please select option '1' if you would like to\n")
    print(Fore.CYAN + "view this weeks playlist\n")
    print(Fore.MAGENTA + "Please select option '2' if you would like to")
    print(Fore.MAGENTA + "enter in a new song to the playlist.\n")

    return view_or_add()


def view_or_add():
    """
    The route the user takes to either view songs from the playlist or
    add songs to the playlist.
    """
    route = input("Please choose either (1 to view) or (2 to submit)\n")

    print("You selected: " + route)
    if route == "1":
        view_songs()
    elif route == "2":
        submit_song()
    else:
        print(Back.RED + Fore.WHITE + "\nIncorrect value. Must be 1 or 2.\n")
        return view_or_add()


def view_songs():
    """
    This function will show all the songs on the playlist which
    """
    list_of_lists = SHEET.worksheet("tunes").get_all_values()
    print(tabulate(list_of_lists))
    return quit_or_repeat()


def quit_or_repeat():
    """
    Start program again to the main menu or quit the program
    """
    print("Please select '1' if you would like to go back to main menu\n")
    print("Or '2' if you would like to quit\n")

    route = input("Please choose either (1 to repeat) or (2 to quit)")

    print("You selected: " + route)
    if route == "1":
        weekly_playlist_welcome()
    elif route == "2":
        sys.exit(Back.RED + Fore.WHITE + "\nThank you for stopping by!")
    else:
        print(Back.RED + Fore.WHITE + "\nIncorrect value. Must be 1 or 2.\n")
        return quit_or_repeat()


def submit_song():
    """
    This function will allow users to add and update songs
    to the playlist
    """

    artist = None
    song = None

    while True:
        artist = input(Fore.CYAN + "\nPlease input the artist's name\n")

        if artist.replace(' ', '').isalpha():
            break
        else:
            print("Invalid! Please alphabet characters only")

    while True:
        song = input(Fore.CYAN + "\nPlease input the song name\n")

        if song.replace(' ', '').isalpha():
            break
        else:
            print("Invalid! Please alphabet characters only")

    SHEET.worksheet("tunes").append_row([artist.title(), song.title()])

    print("Updating playlist now.....\n")

    print(Back.YELLOW + Fore.BLUE + "Playlist has been updated!\n")
    return quit_or_repeat()


submit_song()


def main():
    """
    Main function is used to run the program
    """
    weekly_playlist_welcome()
    view_or_add()


main()

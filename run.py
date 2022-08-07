"""
Import APIs and colorama library
"""
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

    print("Please select option '1' if you would like to\n")
    print("view this weeks playlist\n")
    print("Please select option '2' if you would like to")
    print("enter in a new song to the playlist.\n")

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

    route = input("Please choose either (1 to start again) or (2 to quit)")

    print("You selected: " + route)
    if route == "1":
        return weekly_playlist_welcome()
    elif route == "2":
        print("Thank you for listening")


def submit_song():
    """
    This function will allow users to add and update songs
    to the playlist
    """
    artist = input("\n Please input the artist's name\n")

    song = input("\n Please input the song name\n")
    SHEET.worksheet("tunes").append_row([artist, song])

    print("Updating playlist now.....\n")

    print("Playlist has been updated!\n")
    return quit_or_repeat()


def main():
    """
    Main function is used to run the program
    """
    weekly_playlist_welcome()
    view_or_add()


main()

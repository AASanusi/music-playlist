"""
Import APIs and colorama library
"""
import sys
from tabulate import tabulate
import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('music_playlist')


def music_playlist_welcome():
    """
    Introducing and informing the user about
    the application.
    """
    print(Fore.YELLOW + Style.BRIGHT + 'WELCOME MUSIC LOVERS!')
    print(Fore.YELLOW + Style.BRIGHT + 'TO THE BEST "MUSIC PLAYLIST" EVER!\n')
    print(Fore.GREEN + Style.BRIGHT + 'Listening to music is life.')
    print(Fore.GREEN + Style.BRIGHT + 'Use this playlist to check out songs')
    print(Fore.GREEN + Style.BRIGHT + 'and add your own songs.\n')

    print("Please select option '1' if you would like to\n")
    print("view the music playlist\n")
    print("Please select option '2' if you would like to")
    print("enter in a new song to the playlist.\n")

    return view_or_add()


def view_or_add():
    """
    The route the user takes to either view songs from the playlist or
    add songs to the playlist.
    """
    route = input(Fore.MAGENTA + "Please choose: 1 to view or 2 to submit\n")

    print("You selected: " + route)
    if route == "1":
        view_songs()
    elif route == "2":
        submit_song()
    else:
        print(Fore.WHITE + "\nIncorrect value. Must be 1 or 2.\n")
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

    route = input(Fore.MAGENTA + "Please choose: 1 to repeat or 2 to quit\n")

    print("You selected: " + route)
    if route == "1":
        music_playlist_welcome()
    elif route == "2":
        sys.exit(Fore.RED + Style.BRIGHT + "\nThank you for stopping by!\n")
    else:
        print(Fore.WHITE + "\nIncorrect value. Must be 1 or 2.\n")
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

    print(Fore.WHITE + "Updating playlist now.....\n")

    print(Fore.YELLOW + Style.BRIGHT + "Playlist has been updated!\n")
    return quit_or_repeat()


def main():
    """
    Main function is used to run the program
    """
    music_playlist_welcome()
    view_or_add()


main()

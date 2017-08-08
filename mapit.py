#!/usr/local/bin/python3

import webbrowser, pyperclip
from sys import argv

# mapit - Launches a map in the browswer using an address from the command line
# or clipboard (Must install pyperclip pip3 install pyperclip)

def location(address):
    # Get the address
    address = ' '.join(argv[1:])
    if argv < 1:
        # Get address from clipboard
        address = pyperclip.paste()
        webbrowser.open('https://www.google.com/maps/place/' + address)

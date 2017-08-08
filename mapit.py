#!/usr/local/bin/python3

import webbrowser, pyperclip
from sys import argv

if len(argv) > 1:
    # Get address from command line.
    address = ' '.join(argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

#!/usr/bin/env python3

"""Retrive and print words from UTF-8 document"""


import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from
        the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """ Print items one per line

        Args:
            An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text focument from an url

    Args:
        url: The URL of UTF-8 text document
     """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])

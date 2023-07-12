#!/usr/bin/python3
"""Module that executes a function that appends a line."""


def append_after(filename="", search_string="", new_string=""):
    """Function that appends a new line when a string is found.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename, 'r', encoding="utf-8") as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)

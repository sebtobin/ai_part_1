"""
COMP30024 Artificial Intelligence, Semester 1, 2022
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""

import sys
import json

# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
from search.util import print_board, print_coordinate

from search.pathfinding import search_path

def main():

    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)

    # TODO:
    # Find and print a solution to the board configuration described
    # by `data`.
    # Why not start by trying to print this configuration out using the
    # `print_board` helper function? (See the `util.py` source code for
    # usage information).

    print(data)

    board_dict = {}
    for tile in data["board"]:
        board_dict[(tile[1], tile[2])] = tile[0]

    board_dict[(data["start"][0], data["start"][1])] = "start"
    board_dict[(data["goal"][0], data["goal"][1])] = "goal"

    print_board(data["n"], board_dict)

    search_path(data["start"], data["goal"])


# HI PEPUCHINO

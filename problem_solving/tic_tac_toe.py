# Implement a game of tic-tac-toe
import random
# create an empty board as a list
# create a function to format the board with spaces separated by a pipe
# set different areas of the board according to their index
# create a function called play
# set a list of winning combinations
# let the user know they are "X"
# Prompt the user to pick a space

board = range(0,9)
open_spaces = list(range(0,9))
winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8],
           [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]


def show():
    """Displays the board in the right format with numbered spaces"""
    print "-" * 10
    print board[0], "|", board[1], "|", board[2]
    print "-" * 10
    print board[3], "|", board[4], "|", board[5]
    print "-" * 10
    print board[6], "|", board[7], "|", board[8]
    print "-" * 10


def win_check():
    """ Checks to see who won the game"""


def play():
    """ plays the game of tic tac toe"""
    while True:
        choice = int(raw_input("Pick an open number from the board >>> "))
        if choice != "X" and choice != "O":
            board[choice] = "X"
            open_spaces.remove(choice)
        else:
            print "This spot is already taken"
        show()

        comp_choice = random.choice(open_spaces)
        print "The computer picked area %s" % (comp_choice)
        board[comp_choice] = "O"
        open_spaces.remove(comp_choice)
        win_check()

play()

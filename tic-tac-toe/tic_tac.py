import unittest
from itertools import chain

class TryAgainError(Exception):
    pass

def play():
    default_grid_size = 3
    current_board = setup_board(default_grid_size)

    print("Welcome to tic tac toe, lets play.")

    player = "x"
    game_over = False
    while not game_over:
        try:
            print(f"Player {player}'s turn.")
            for row in current_board:
                print(' '.join(row)) 
            selection = input(f"Select one of the open spaces on the current board between 0 - {str(default_grid_size**2)}\n >> ")
            if not valid_input(selection, current_board):
                continue

            if board_full(current_board):
                print("booooo, lame it's a tie")
                game_over = True

            current_board = update_board(selection, current_board, player)
            if is_winner(current_board, player):
                game_over = True


            player = "x" if player == "o" else "o"
        except:
            TryAgainError("Please try again")

def setup_board(grid: int):
    """Creates the board for the player to play on"""
    board =[]
    for _ in range(grid):
        row = []
        for _ in range(grid):
            row.append(".")
        board.append(row)
    return board

def valid_input(selection: int, board: list[list]) -> int:
    """Prompts the player to select one of the open spaces."""

    flat_board = list(chain(*board))
    valid_selections = [cell for cell in flat_board if cell == "."]

    try:
        int(selection)
    except ValueError:
        raise TryAgainError("Please select a valid integer")
    
    try:
        cell = flat_board.index(selection)
    except ValueError:
        raise TryAgainError(f"Please select a valid integer {[valid_selections]}")


    if cell == "x" or cell == "o":
        raise TryAgainError(f"Please select a valid integer that isn't already selected. Valid selections: {valid_selections} ")
    return int(selection)

def update_board(grid, selection, board, player) -> list[list]:
    """Update board with current players selection by updating the guess to a 2D array."""
    
    col_i = selection % grid
    row_i = selection // grid

    board[col_i][row_i] == player
    return board

def is_winner(board: list[list], player) -> bool:
    """Checks to see if player has won"""

    for row in board:
        if all(cell == player for cell in row):
            return True

    if col_winner(board, player):
        return True

    if diagonal_winner(board, player):
        return True
    return False
    

def col_winner(board: list[list], player) -> bool:
    """Search for the """
    col_len = len(board[0])

    for x in range(col_len):
        for i, row in enumerate(board):
            if row[x] != player:
                break
            elif i == col_len - 1:
                return True
    return False


def diagonal_winner(board: list[list], player) -> bool:
    return _diagonal_forward(board, player) or _diagonal_backward(board, player)


def _diagonal_forward(board: list[list], player):
    match = True
    x = 0
    y = 0

    max_index = len(board[0]) - 1
    while match and x < max_index:
        if board[x][y] != player:
            match = False
        x = y = x+1
    return match

def _diagonal_backward(board: list[list], player):
    x = 0
    y = -1
    match = True
    max_index = len(board[0]) - 1
    while match or x < max_index and abs(y) < max_index:
        if board[x][y] != player:
            match = False
        y -= 1
        if abs(y) < max_index:
            x += 1
            y = -1
    return match


def board_full(board: list[list]):
    return all(False for row in board for cell in row if cell == ".")



class TestTicTacFns(unittest.TestCase):

    def test_setup_board(self):
        self.assertEqual(setup_board(3), [[".", ".", "."], [".", ".", "."], [".", ".", "."]])
    
    def test_invalid_input_non_int(self):
        with self.assertRaises(TryAgainError):
            valid_input("hi", [["."]])
    
    def test_invalid_input_already_selected(self):
        with self.assertRaises(TryAgainError):
            valid_input(2, [[".", ".", "."]])

    def test_invalid_input_out_of_range(self):
        with self.assertRaises(TryAgainError):
            valid_input(10, [[".", ".", "."], [".", ".", "."], [".", ".", "."]])
    
    def test_board_full(self):
        self.assertTrue(board_full([["x", "o", "x"], ["o", "x", "o"], ["o", "x", "o"]]))
        self.assertFalse(board_full([["x", "."], ["o", "x"]]))

    def test_col_winner(self):
        winners = [
            [["x", "x", "o"], ["o", "x", "o"], [".", "x", "."]],
            [["x", "o", "x"], ["x", "o", "."], ["x", ".", "o"]],
            [[".", "o", "x"], ["o", ".", "x"], [".", "o", "x"]]
                   ]
        
        for winner in winners:
            self.assertTrue(col_winner(winner, "x"))


        losers = [[["x", ".", "o"], [".", ".", "."], [".", "x", "o"]]]

        for l in losers:
            self.assertFalse(col_winner(l, "x"))
    
    def test_row_winner(self):
        winners = [
                   [["x", "x", "x"], ["o", ".", "o"], [".", "x", "o"]], 
                   [["o", ".", "o"], ["x", "x", "x"], [".", "x", "o"]],
                   [["o", ".", "o"], [".", "x", "o"], ["x", "x", "x"]]
                   ]
        
        for winner in winners:
            self.assertTrue(is_winner(winner, "x"))

        losers = [[["x", "o", "x"], ["o", ".", "o"], [".", "x", "o"]],
                   [[".", ".", "o"], [".", ".", "."], [".", "x", "o"]],
                   [["o", ".", "o"], [".", "x", "o"]], [".", "x", "o"]]
        
        losers = [[[".", ".", "o"], [".", ".", "."], [".", "x", "o"]]]

        for l in losers:
            self.assertFalse(is_winner(l, "x"))


if __name__ == "__main__":
    # unittest.main()

    play_game = True
    while play_game:
        play()

        play_again = input('Would you like to play again, type "y" yes.  All other input will end the game')
        if play_again != "y":
            play_game = False

    print("Thanks for playing! Byeeeeee")
 

def tic_tac_random():
    """Play game of tic-tac-toe.

    The human will be X and the computer will be O.

    Loop:
    - Show the board
    - If it's the human's turn, prompt for a position (1-9) and make their move
    - If it's the computer's turn, make any legal move
    - If there's a winner or the board is full, quit the game

    At the end of the game, announce the winner (if any).
    """

    board = setup_board()
    current_player = 'X'
    winner = None

    while not winner and not is_board_full(board):
        print_board(board)
        if current_player == 'X':
            selection = input("\nEnter move (1-9)> ")
            move = validate_move(selection, board)

            position = int(move)
            make_move(board, position, 'X')
            current_player = 'O'
        else:
            position = make_random_move(board, 'O')
            print("O played in position %s" % position)
            current_player = 'X'

        winner = find_winner(board)

    if winner:
        print("Congratulations to " + winner)
    else:
        print("How boring, a tie")


def setup_board():
    """Create an empty tic-tac-toe board.

    Create a board as a list-of-rows, each row being a list-of-cells.

    Put '.' in each cell to mark it as empty.

    Return the board.

    >>> setup_board()
    [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    """

    return [['.', '.', '.'],['.', '.', '.'],['.', '.', '.']]


def is_board_full(board):
    """Return True is board is full, False otherwise.

    >>> is_board_full([['.', '.', '.'], ['X', '.', 'O'], ['.', '.', '.']])
    False

    >>> is_board_full([['X', 'O', '.'], ['X', 'O', 'X'], ['X', 'O', 'X']])
    False

    >>> is_board_full([['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'O', 'O']])
    True
    """

    for row in board:
        if "." in row:
            return False
    return True
    
def validate_move(move, board):
    while True:
        if not move.isdigit() or not (1 <= int(move) <= 9):
            move = input("Invalid input. Enter a number between 1 and 9: ")
            continue

        position = int(move)
        row, col = divmod(position - 1, 3)
        if board[row][col] != '.':
            move = input("Spot is taken. Try again (1-9): ")
            continue

        return move


def make_random_move(board, player):
    """Find an empty cell and play into it.

    player = 'X' or 'O', depending on who should move.

    This will change the board in-place. It should return the
    position (1-9) it played into.

    You don't need to do this randomly -- it can simply use the first empty
    cell it finds.

    >>> board = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'O', '.']]
    >>> make_random_move(board, 'X')
    9

    >>> board
    [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'O', 'X']]
    """
    for ri, row in enumerate(board):
        for i, cell in enumerate(row):
            if cell == ".":
                board[ri][i] = player
                return i + 1


def find_winner(bd):
    """"Given board, determine if winner. Return 'X', 'O', or None if no winner.

    >>> print find_winner([['.', '.', '.'], ['X', '.', 'O'], ['.', '.', '.']])
    None

    >>> find_winner([['X', '.', '.'], ['X', '.', 'O'], ['X', '.', '.']])
    'X'

    >>> find_winner([['X', 'O', 'X'], ['O', 'O', 'X'], ['O', 'X', 'X']])
    'X'

    >>> find_winner([['X', '.', 'O'], ['X', 'O', 'O'], ['O', '.', '.']])
    'O'
    """
    # Check for win in each row
    for row in bd:
        if row[0] != "." and len(set(row)) == 1:
            return row[0]

    # check for win in each column
    for coli in range(3):
        if bd[0][coli] != "." and bd[0][coli] == bd[1][coli] == bd[2][coli]:
            return bd[0][coli]

    # check for diagnol /
    if bd[0][0] != "." and bd[0][0] == bd[1][1] == bd[2][2]:
        return bd[0][0]

    # check for diagnol \
    if bd[0][2] != "." and bd[0][2] == bd[1][1] == bd[2][0]:
        return bd[2][0]


def print_board(board):
    """Given a board[col][row], print it out.

    >>> print_board([['.', '.', '.'], ['X', '.', 'O'], ['.', '.', '.']])
    . . .
    X . O
    . . .
    """

    for row in board:
        for cell in row:
            print(cell + " ", end="")
        print()


def make_move(board, position, player):
    """Play into position 1-9.

    position = 1-9 (top-left, top-middle, top-right ... bottom-right)
    player = 'X' or 'O'

    This should update the board to play there. It does not return anything.

    >>> board = [['X', '.', 'O'], ['X', 'O', 'O'], ['O', '.', '.']]

    >>> make_move(board, 2, 'O')
    >>> board
    [['X', 'O', 'O'], ['X', 'O', 'O'], ['O', '.', '.']]

    >>> make_move(board, 9, 'X')
    >>> board
    [['X', 'O', 'O'], ['X', 'O', 'O'], ['O', '.', 'X']]
    """

    # divmod gives you the the floor division of 2 numbers and the % of the 2 numbers
    # position - 1 is the index
    # 3 is the number of spaces in the row

    coli, rowi = divmod(position - 1, 3)

    board[coli][rowi] = player


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        import doctest

        if doctest.testmod().failed == 0:
            print("\n*** ALL TESTS PASS. FANTASTIC WORK!\n")
    else:
        tic_tac_random()



def street_fighter_selection(fighters, initial_position, moves):
#     fighters = [
#       ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
#       ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
# ]

# set an ans list to append the fighters to
    ans = []
#     starting position is Ryu (0,0)
    row = fighters[0]
    col = fighters[0][0]
    
#     current position is the position of the fighter we are currently on
    current_position = initial_position
    
#     current row/col
    current_row = current_position[0]
    current_col = current_position[1]
    
# loop over the list of moves we were given
    for move in moves:
#     change the row for up/down
# set a base case for being at the top or bottom of the rows
        if move == "up":
            current_row = current_row - 1
            if current_row <= 0:
                current_row = 0
        elif move == "down":
            current_row = current_row + 1
            if current_row >= 1:
                current_row = 1
#         if the moves are left or right, move the col
        elif move == "left" and current_col != 0:
            current_col = current_col - 1
        elif move == "left" and current_col == 0:
#         if we are at the end of the col, the current col is the len of the row - 1
            current_col = len(fighters[0]) - 1
        elif move == "right" and current_col != 5:
            current_col = current_col + 1
        elif move == "right" and current_col == 5:
            current_col = 0
        ans.append(fighters[current_row][current_col])

    return ans
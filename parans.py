def solve(st, idx):
    # check to see if the given index at the string is "("
        # if it isn't return -1 for a fail fast approach
    if st[idx] != "(":
        return -1

    # set an open parens counter
    open_par = 0

    # enumerate over the string, starting at the given index + 1
    for i, ch in enumerate(st[idx + 1:]):
        # if we find another open parens, add one to the counter
        if ch == "(":
            open_par += 1
        elif ch == ")":
            if not open_par:
                return i + idx + 1
            open_par -= 1




def solve(st, idx):
#     check to see if the idx is actually a "("
    if st[idx] is not "(":
        return -1
        
#     set up amn open parens count
    open_parens = 0
    for i, char in enumerate(st[idx + 1:]):
        if char == "(":
            open_parens += 1
        elif char == ")":
            if open_parens == 0:
                return i+ idx + 1
            open_parens -= 1
    return -1
            
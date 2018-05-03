# I like parentheticals (a lot).

# "Sometimes (when I nest them
    # (my parentheticals) too much (like this (and this))) they get confusing."

# Write a method that, given a sentence like the one above,
# along with the position of an opening parenthesis, finds the corresponding closing parenthesis.

# Example: if the example string above is input with the number 10 
# (position of the first parenthesis), the output should be 79 (position of the last parenthesis).


# define a function that takes in a string and an index
def find_parens(string, index):
    """Finds the matching closing parens"""
    # check if the index is a "("
    # if it isn't, return false
    open_parens = 0
    if string[index] != "(":
        return None
    # if it is, loop through the index, starting at our given index + 1
    for s_index, char in enumerate(string[index + 1:]):
        # if we find an open parenthesis, add one to an open parens counter
        if char == "(":
            open_parens += 1
        # if we find a closing ")", if open_ parens = 0 return slice_index + given_index + 1
        if char == ")":
            if open_parens == 0:
                # add the last +1 because the problem asked for the position
                return index + 1 + s_index + 1
        # else: open parens -= 1
            else:
                open_parens -= 1
    return None

find_parens("Sometimes (when I nest them(my parentheticals) too much (like this (and this))) they get confusing.", 10)







    # to get the correct indicies of the slice, we need to add given index + 1 + slice_index
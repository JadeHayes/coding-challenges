"""Using a binary search, find val in a range of 1-100. Return # of guesses.

Construct a list of 1-100 (inclusive). Write a binary search that searches
for val in that list (val will always be a number between 1 and 100).

Return the number of searches it took to find val. For a proper binary search
of 1-100, this should never be more than 7.

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7
"""
 # assert 0 < val < 101, "Val must be between 1-100"

    # num_guesses = 1
    # guess = 50
    # minimum = 0
    # maximum = 100

    # while guess != val:
    #     if guess < val:
    #         minimum = guess
    #         guess = (maximum + minimum)/2
    #     elif guess > val:
    #         maximum = guess
    #         guess = (minimum + maximum)/2
    #     num_guesses += 1
    # return num_guesses


def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""
    guess = 50
    counter = 1
    minimum = 1
    maximum = 100

    while guess != val:
        if guess > val:
            maximum = guess
            guess = (maximum + minimum) / 2
        elif guess < val:
            minimum = guess
            guess = (maximum + minimum) / 2
    if counter > 8:
        return "False information provided"
    else:
        return "Test was honest"




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n"

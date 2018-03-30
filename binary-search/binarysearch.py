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


def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 1
    minimum = 0
    maximum = 101
    # Set the guess to 1/2 the max value, this way you eliminate half of the possibilities
    guess = 50
    # set a while loop that runs until the guess and val are the same

    while guess != val:
        # set conditionals that check if the guess is higher or lower than the value
        if guess < val:
        # if it is lower, guess becomes the new min
            minimum = guess
        # if it is higher, guess becomes the new max
        elif guess > val:
            maximum = guess
        # set the new guess to the midway point (min + max) / 2
        guess = (minimum + maximum)/2
        num_guesses += 1

    return num_guesses


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n"

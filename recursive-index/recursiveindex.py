"""Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

For example:

    >>> recursive_index(5, [1, 3, 5, 2, 4])
    2

    >>> recursive_index("hey", ["hey", "there", "you"])
    0

    >>> recursive_index("you", ["hey", "there", "you"])
    2

    >>> recursive_index("zork", ["foo", "bar", "baz"]) is None
    True

"""
# Recursive


def recursive_index(needle, haystack, counter=0):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """

    # check if there is a list
    if not haystack:
        return None
    # look through the list by the 0th item
    # counter start at zero

    elif haystack[0] == needle:
        return counter
    # is the 0th item the needle?
    # return counter (0)

    # if not, recursively call remainder of the list pass in counter + 1
    return recursive_index(needle, haystack[1:], counter + 1)


################################################################################
# With helper

def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """

    def _recursive_index(needle, haystack, counter):
        """helper function to track the counter(index)"""

        # check if there is a list
        if counter == len(haystack):
            return None
        # look through the list by the 0th item
        # counter start at zero

        elif haystack[counter] == needle:
            return counter
        # is the 0th item the needle?
        # return counter (0)

        # if not, recursively call remainder of the list pass in counter + 1
        return _recursive_index(needle, haystack, counter + 1)

    return _recursive_index(needle, haystack, 0)


################################################################################
# With While loop

def recursive_index(needle, haystack, counter=0):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """

    counter = 0

    while counter < len(haystack):
        if haystack[counter] == needle:
            return counter
        counter += 1




    # an essay about essays by paulgraham.com/essay/html





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO GO GO!\n"

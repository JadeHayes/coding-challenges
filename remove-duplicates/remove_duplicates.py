""" Remove duplicates in a list

For example::

    >>> remove_duplicates([6, 9, 7, 9, 2, 6, 0])
    [6, 9, 7, 2, 0]

    >>> remove_duplicates([])
    []

    >>> remove_duplicates([6, 9, 7])
    [6, 9, 7]

"""


def remove_duplicates(items):
    """Remove duplicates in the list items and return that list."""
    ## wont work b/c the list wants it in the same order
    # nums = list(set(items))
    # return nums

    # loop over the list
    # append num to a new list
    # if the num in our loop is also in our new list, skip it
    ans = []
    for num in items:
        if num not in ans:
            ans.append(num)
    return ans

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"




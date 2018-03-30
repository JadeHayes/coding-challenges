"""How much rain is trapped in Codelandia?

No buildings mean no rain is captured::

    >>> rain([])
    0

All-same height buildings capture no rain::

    >>> rain([10])
    0

    >>> rain([10, 10])
    0

    >>> rain([10, 10, 10, 10])
    0

If there's nothing between taller buildings, no rain is captured::

    >>> rain([2, 3, 10])
    0

    >>> rain([10, 3, 2])
    0

If two tallest buildings are same height and on ends, it's easy::

    >>> rain([10, 5, 10])
    5

    >>> rain([10, 2, 3, 4, 10])
    21

    >>> rain([10, 4, 3, 2, 10])
    21

    >>> rain([10, 2, 4, 3, 10])
    21

If two tallest buildings are ends, but not the same height,
it will fall off the shorter of thh two::

    >>> rain([10, 2, 3, 4, 9])
    18

Rain falls off the left and right edges::

    >>> rain([2, 3, 10, 5, 5, 10, 3, 2])
    10

Trickier::

    >>> rain([2, 3, 1, 4, 3, 10, 7, 10, 5, 4, 3, 6, 2, 5, 2])
    15

Should also work with floats::

    >>> r = rain([4.5, 2.2, 2.2, 4])
    >>> round(r, 2)
    3.6
"""


def rain(buildings):
    """How much rain is trapped in Codelandia?"""
    # max building height var
    current_index = 0
    # next index
    # i = 1

    total = 0

    if len(buildings) <= 2:
        return total

    while current_index <= len(buildings)-2:
        i = current_index + 1
        current = buildings[current_index]
        got_to_end = False

        while current < buildings[i]:
            if i < len(buildings) - 1:
                got_to_end = True
                break
            i += 1
        if got_to_end:
            maximum = 0
            max_i = 0
            for index, num in enumerate(buildings[current_index:]):
                if num > maximum:
                    maximum = num
                    max_i = index

            j = current_index + 1
            while j < max_i:
                total += maximum - buildings[j]
                j += 1
            current_index = max_i

        else:
            j = current_index + 1

            while j <= i:
                total += current - buildings[j]
                j += 1
            current_index = j
    return total



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"

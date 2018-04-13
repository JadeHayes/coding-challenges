"""Split a string by splitter and return list of splits.

This should work like the built-in Python .split() method [*].
YOU MAY NOT USE the .split() method in your solution!
YOU MAY NOT USE regular expressions in your solution!

For example:

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

* Note: the actual Python split method has special behavior
  when it is not passed anything for the splitter -- you do
  not need to implement that.

"""


#FIXME
def split(astring, splitter):
    """Split a string by splitter and return list of splits."""
    # answer list to store the string that we split
    ans_lst = []
    index = 0
    # for char in enumerate string
    while index <= len(astring):

        curr_index = index
        index = astring.find(splitter, index)

        if index != -1:
            ans_lst.append(astring[curr_index:index])
            index += len(splitter)

        else:
            ans_lst.append(astring[curr_index:])
            break
    return ans_lst


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. FINE SPLITTING!\n"

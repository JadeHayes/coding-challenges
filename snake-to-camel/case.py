"""Given a variable name in snake_case, return camelCase of name.

For example::

    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'

"""


def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name."""
    # split the variable name by the underscore
    variable_name = variable_name.split("_")
    snake_case = ""
    # for each word in the list
    for word in variable_name:
        # not including the first word
        if word != variable_name[0]:
            # title and concatenate to a snake case string
            snake_case += word.title()
        else:
            # add the first word without capitalizing the first letter
            snake_case += word
    # return the concatenated version of snake_case
    return snake_case



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"

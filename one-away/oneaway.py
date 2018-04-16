"""Given two strings, are they, at most, one edit away?

    >>> one_away("make", "make")
    True

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask" ,"asks")
    True

    >>> one_away("asks", "ask")
    True

    >>> one_away("act", "tact")
    True

    >>> one_away("fat", "fact")
    True

    >>> one_away("yes", "no")
    False

"""


def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""
    # # setup a dictionary to count the amount of times a char is present
    # # for each w1 & w2

    # # loop through the longer dictionary,check to see if the difference of the val
    # # of the oppo dict is > 1
    # w1d = {}
    # w2d = {}

    # # Fail fast if the len difference is > 1
    # # then there is no waywewould be 1 off
    # if abs(len(w1) - len(w2)) > 1:
    #     return False

    # # setting up a dictionary count for w1
    # for char1 in w1:
    #     w1d[char1] = w1d.get(char1, 0) + 1

    # # setting up a dictionary count for w2
    # for char2 in w2:
    #     w2d[char2] = w2d.get(char2, 0) + 1

    # # finding the shorter dictionary to go
    # if len(w1d) > len(w2d):
    #     shorter, longer = w2d, w1d
    # else:
    #     shorter, longer = w1d, w2d

    # # loop overand compare the dictionary values of w1d w2d
    # for key, val in longer.iteritems():
    #     # if the value in the dictionary
    #     if shorter.get(key, -1) - int(val) > 1:
    #         return False

    # vals = shorter.values()
    # if vals.count(-1) > 1:
    #     return False

    # return True




    # fail fast by checking the length, if one word is > the other by more than
    # 1 char, we fail fast. 
    # set up a while loop to compare the indicies, add one to the index if matches
    wrong = 0

    # Check to see if the length of the words vary by more than one
    if abs(len(w1) - len(w2)) > 1:
        return False

    # check to see which word is shorter, in our case, the shorter word will always
    # be w2

    if len(w1) < len(w2):
        w1, w2 = w2, w1

    i = 0
    j = 0

    # while the second index is shorter than the shorter word
    while j < len(w2):
        if w1[i] != w2[j]:
            # we found a wrong letter
            wrong += 1

            if wrong > 1:
                return False

            # lets move back to the next iteration of the longer string
            i += 1

            # if they are the same length,increase j too
            if len(w1) == len(w2):
                j += 1

        else:
            i += 1
            j += 1
    return True





    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; NICE JOB! ***\n"

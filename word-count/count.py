"""Count words in a sentence, and print in ascending order.

For example::

    >>> word_count("berry cherry cherry cherry berry apple")
    apple: 1
    berry: 2
    cherry: 3

If there is a tie for a count, make sure the words are printed in
ascending order within the tie::

    >>> word_count("hey hi hello")
    hello: 1
    hey: 1
    hi: 1

Capitalized words are considered distinct::

    >>> word_count("hi Hi hi")
    Hi: 1
    hi: 2
"""
# create a function that takes in a string of words

# split the sentance by " " and save into list
# set an empty dictionary for word and count
# loop over the list and add each word to a dictionary with a +1 count
# get the values and sort them [1,2,3]
# loop over the list
# loop over dictionary using iteritems.
# if the value is the same as the current, print it


def word_count(phrase):
    """Count words in a sentence, and print in ascending order."""

    word_count_dict = {}
    counts = []

    for word in phrase.split(" "):
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

    for word, val in word_count_dict.iteritems():
        counts.append((val, word))

    counts.sort()
    for count, word in counts:
        print "{key}: {val}".format(key=word, val=count)





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; NICE JOB! ***\n"

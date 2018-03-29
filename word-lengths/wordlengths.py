"""Get dictionary of word-length: {words}.

Given a phrase, return dictionary keyed by word-length, with the value for
each length being the set of words of that length.

For example::

    >>> answer = word_lengths("cute cats chase fuzzy rats")

This should return {4: {'cute', 'cats'}, 5: {'chase', 'fuzzy', 'rats'}},
but since both dictionaries and sets are unordered, we can't just check if
it matches that exact string, so we'll test more carefully::

    >>> sorted(answer.keys())
    [4, 5]

    >>> answer[4] == {'cute', 'cats', 'rats'}
    True

    >>> answer[5] == {'chase', 'fuzzy'}
    True

Punctuation should be considered part of a word, so you only need to
split the string on whitespace::

    >>> answer = word_lengths("Hi, I'm Balloonicorn")

    >>> sorted(answer.keys())
    [3, 12]

    >>> answer[3] == {'Hi,', "I'm"}
    True

    >>> answer[12] == {"Balloonicorn"}
    True
"""


def word_lengths(sentence):
    """Get dictionary of word-length: {words}."""
    # loop over the sentence
    # add len to key value of dictionary
    # add word to value as a set
    words = {}

    for word in sentence.split():
        if words.get(len(word)):
            words[len(word)].add(word)
        else:
            words[len(word)] = {word}
    return words


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NOTHING ESCAPES YOU!\n"

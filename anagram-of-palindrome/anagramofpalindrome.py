"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""
    # palindrome has either exactly 2 of each letter in the word
    # or two of each letter revolving around one in the middle
    # An anagram rescrambles the letters
    chars = []

    # loop over the word
    # append chars to the list
    # if we see the char in list again, remove it.
    # if there is only one char or no chars in list
    # return True
    # else, return false

    for char in word:
        if char in chars:
            chars.remove(char)
        else:
            chars.append(char)
    if len(chars) >= 2:
        return False
    else:
        return True




if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"

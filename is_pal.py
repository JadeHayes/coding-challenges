# Write an efficient method that checks whether any permutation ↴ of an input string is a palindrome. ↴

# You can assume the input string only contains lowercase letters.

# Examples:

# "civic" should return true
# "ivicc" should return true
# "civil" should return false
# "livci" should return false


def is_palindrome(word):
    """checks if any permutation of string is a palindrome."""

    # each set of letters has a pair OR has 1 that it can rotate around
    # set up a dictionary key (letter) : count
    # loop through the values of the dictionary
    word_dict = {}
    odd = 0
    for letter in word:
        word_dict[letter] = word_dict.get(letter, 0) + 1

    for count in word_dict.values():
        if count % 2 != 0:
            odd += 1
        # if odd_count > 1 --> return false
        if odd > 1:
            return False
    # else: return true
    return True

is_palindrome("civic")
is_palindrome("ivicc")
is_palindrome("civil")
is_palindrome("livci")
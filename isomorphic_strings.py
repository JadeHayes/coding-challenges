
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.

import unittest

def is_isomorphic(s: str, t: str):
    letters_map = {}
    for i, letter in enumerate(t):
        mapped_letter = letters_map.get(letter)
        if not mapped_letter and s[i] not in letters_map.values():
            letters_map[letter] = s[i]
        else:
            if mapped_letter != s[i]:
                return False
    return True

class TestIsIsomorphic(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_isomorphic("egg", "add"))
        self.assertTrue(is_isomorphic("paper", "title"))
        self.assertTrue(is_isomorphic("paper", "paper"))


    def test_false(self):
        self.assertFalse(is_isomorphic("foo", "bar"))
        self.assertFalse(is_isomorphic("badc", "baba"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the 
# characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" 
# while "aec" is not).

import unittest

def subsequence(s: str, t: str):
    if s == "" or s == t:
        return True

    i = j = 0
    while j < len(t) and i < len(s):
        if s[i] == t[j]:
            i += 1
            j += 1
            if i >= len(s):
                return True
        else:
            j += 1
            if j >= len(t):
                return False

class TestSubsequence(unittest.TestCase):

    def test_true(self):
        self.assertTrue(subsequence("ace", "abcde"))
        self.assertTrue(subsequence("abc", "ahbgdc"))
        self.assertTrue(subsequence("", ""))


    def test_false(self):
        self.assertFalse(subsequence("b", "c"))
        self.assertFalse(subsequence("hello", ""))

if __name__ == "__main__":
    unittest.main(verbosity=2)



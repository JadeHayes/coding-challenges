import unittest
from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    counter = Counter(magazine)

    i = 0
    while i < len(ransomNote):
        count = counter.get(ransomNote[i])
        if count is None:
            return False
        if count >= 1:
            counter[ransomNote[i]] = count - 1
            i += 1
        else:
            return False
    return True

class TestCanConstruct(unittest.TestCase):
    
    def test_true(self):
        self.assertTrue(canConstruct("b", "bc"))
        self.assertTrue(canConstruct("cab", "abc"))


    def test_false(self):
        self.assertFalse(canConstruct("a", "hi"))
        self.assertFalse(canConstruct("hello", ""))

if __name__ == "__main__":
    unittest.main(verbosity=2)
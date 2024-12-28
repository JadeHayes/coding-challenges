import unittest


def word_pattern(pattern: str, s: str):
    words = s.split()

    if len(pattern) != len(words):
        return False

    pattern_words = {}
    i = 0

    while i < len(pattern):
        current_letter = pattern[i]
        current_word = words[i]
        mapped_word = pattern_words.get(current_letter)
        if not mapped_word:
            if current_word in pattern_words.values():
                return False
            pattern_words[current_letter] = current_word
            i += 1
        else:
            if mapped_word != current_word:
                return False
            i += 1
    return True

class TestWordPattern(unittest.TestCase):

    def test_true(self):
        self.assertTrue(word_pattern(pattern = "abba", s = "dog cat cat dog"))

    def test_false(self):
        self.assertFalse(word_pattern(pattern = "abba", s = "dog cat cat fish"))
        self.assertFalse(word_pattern(pattern = "aaaa", s = "dog cat cat dog"))
        self.assertFalse(word_pattern(pattern = "abba", s = "dog dog dog dog"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
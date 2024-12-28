# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
import unittest

def isHappy(n: int):

    def get_number(num):
        return [int(n) for n in list(str(num))]

    isHappy = False
    while not isHappy:
        next_number = 0
        for number in get_number(n):
            next_number += number^2
        if next_number == 1:
            isHappy = True
        n = next_number
    return isHappy



class TestIsHappy(unittest.TestCase):
    def test_true(self):
        self.assertTrue(isHappy(19))
    def test_false(self):
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)
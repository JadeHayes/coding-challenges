

import unittest

"""
A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

"""

def is_happy(num) -> bool:
        seen = set()
        while num != 1:
             num = sum(int(d)**2 for d in str(num))
             if num in seen:
                return False # endless loop scenario here
             else:
                seen.add(num)
        return True


def nums_squared(nums: list[int]) -> int:
    total = 0
    for n in nums:
        total += n**2
    return total

class TestIsHappy(unittest.TestCase):
    def test_isHappy(self):
        happy_nums = [19]
        for num in happy_nums:
            self.assertTrue(is_happy(num))
    
    def test_isNotHappy(self):
        unhappy_nums = [2]
        for num in unhappy_nums:
            self.assertFalse(is_happy(num))
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)


# Old solution from previous study attempts
# def is_happy(n):
#     # create a set seen, for the sum of the squares we have
#     seen = set()
#     # while the number we get isn't 1
#     while n!=1:
#         # n is the sum of the digits squared and added together
#         n = sum(int(d)**2 for d in str(n))
#         # if n isn't in the seen set, add it.  If it is return False b/c it'll have us in a loop
#         if n not in seen:
#             seen.add(n)
#         else:
#             return False
#     # if this all passes return true
#     return True

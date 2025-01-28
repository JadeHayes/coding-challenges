import unittest
"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
"""

class Node:
    next = None
    prev  = None

def longest_consecutive(nums: list[int]) -> int:
    """
    You must write an algorithm that runs in O(n) time
    Constraints: 0 <= nums.length <= 105 AND -109 <= nums[i] <= 109
    """
    if not nums:
        return 0

    num_set = set(nums)
    longest = 1
    streak = 1

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                streak += 1

            longest = max(longest, streak)
    return longest


class TestLongestConsecutive(unittest.TestCase):
    def test_example_one(self):
        nums = [100,4,200,1,3,2]
        expected = 4
        self.assertEqual(longest_consecutive(nums), expected)

    def test_example_two(self):
        nums = [0,3,7,2,5,8,4,6,0,1]
        expected = 9
        self.assertEqual(longest_consecutive(nums), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
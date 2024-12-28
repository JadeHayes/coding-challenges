from typing import List
import unittest

"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    nums1 has a length of m + n
    m elements denote the elements that should be merged --- this is unclear if it's the index, num of elements, range?
    nums2 has a length of n

    NOTE: the weirdness in the way "non-descending is worded is to let you know when the merge can start (i.e. [1, 2, 0] when next < previous, merge can start)

    Additional TestCases:
    Will there ever be a case where all of the elements in nums 2 wont need to be merged (ex: nums1 = [1,2,0] m = 1 and nums2 = [3, 4] n = 2)?
    """
    nums_insert_index = m
    previous = None
    for i, curr in enumerate(nums1):
        if previous is not None and curr < previous:
            nums_insert_index = i
            break
        previous = curr

    for i, num in enumerate(nums2):
        nums1[nums_insert_index] = num
        nums_insert_index += 1

    nums1.sort()
    

class TestSolution(unittest.TestCase):

    def test_merge(self):
        nums1 = [1,2,3,0,0,0]
        m = 3

        nums2 = [2,5,6]
        n = 3

        expected = [1,2,2,3,5,6]
        merge(nums1, m, nums2, n) 

        self.assertEqual(nums1, expected)
        self.assertEqual(id(nums1), id(nums1))

    def test_empty_m_again(self):
        nums1 = [0,0,0,0,0]
        m = 0
        nums2 = [1,2,3,4,5]
        n = 5

        expected = [1,2,3,4,5]

        merge(nums1, m, nums2, n) 

        self.assertEqual(nums1, expected)
        self.assertEqual(id(nums1), id(nums1))
    
    def test_empty_n(self):
        nums1 = [1]
        m = 1

        nums2 = []
        n = 0

        expected = [1]

        merge(nums1, m, nums2, n) 

        self.assertEqual(nums1, expected)
        self.assertEqual(id(nums1), id(nums1))

    
    def test_empty_m(self):
        nums1 = [0]
        m = 0
        
        nums2 = [1]
        n = 1
        expected = [1]
       
        merge(nums1, m, nums2, n) 
        self.assertEqual(nums1, expected)
        self.assertEqual(id(nums1), id(nums1))

    
    def test_negatives(self):
        nums1 = [-1,-1,0,0,0,0]
        m = 4
        nums2 = [-1,0]
        n = 2

        expected = [-1,-1,-1,0,0,0]

        merge(nums1, m, nums2, n) 

        self.assertEqual(nums1, expected)
        self.assertEqual(id(nums1), id(nums1))
 



if __name__ == "__main__":
    unittest.main(verbosity=2)

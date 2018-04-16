"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8

    [1, 2, 3, 4, 5, 6, 7, 9, 10]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """

    i = 0
    j = 0
    range_maxnum = range(1, max_num + 1)
    nums = sorted(nums)

    while i < len(nums):
        if nums[i] != range_maxnum[j]:
            return nums[i] - 1 
        i += 1
        j += 1







if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. NICELY DONE!\n"

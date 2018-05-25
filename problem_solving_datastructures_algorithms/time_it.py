# timeit.py

# check to see that list index is constant time O(1)
'''To use timeit you create a Timer object whose parameters
are two Python statements. The first parameter is a Python
statement that you want to time; the second parameter is a
statement that will run once to set up the test'''
import timeit

def test1():
    """testing time of list indexing"""
    example = [1, 3, 2, 4, 5, 6, 8, 8, 8, 16, 28, 8]
    return example[3]


def test2():
    """get item for dictionaries"""
    my_dict = {1: None, 3: None, 2: None, 4: None}
    return my_dict[1]


def test3():
    """set item for dictionaries"""
    my_dict = {1: None, 3: None, 2: None, 4: None}
    my_dict[8] = "yay"


def test4():
    """Delete item in a dictionary"""
    my_dict = {1: None, 3: None, 2: None, 4: None}
    del my_dict[3]


def test5():
    """Delete item in a list"""
    example = [1, 3, 2, 4, 5, 6, 8, 8, 8, 16, 28, 8]
    del(example[4])


def smallest(lst):
    """Given a list of numbers in random order, write an algorithm
    that works in O(nlog(n)) to find the kth smallest number in the list."""

    n = len(lst)
    # loop through the list 
    while n > 0:


t1 = timeit.Timer("test1()", "from __main__ import test1")
print "List indexing", t1.timeit(number=1000), "milliseconds"

t2 = timeit.Timer("test2()", "from __main__ import test2")
print "Get item dictionary", t2.timeit(number=1000), "milliseconds"

t3 = timeit.Timer("test3()", "from __main__ import test3")
print "Set item dictionary", t3.timeit(number=1000), "milliseconds"

t4 = timeit.Timer("test4()", "from __main__ import test4")
print "Delete item in a dictionary", t4.timeit(number=1000), "milliseconds"

t5 = timeit.Timer("test5()", "from __main__ import test5")
print "Delete item in a list", t5.timeit(number=1000), "milliseconds"

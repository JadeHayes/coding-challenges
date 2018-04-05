# implement merge sort

# 1) Create a function that takes in an array and splits it into 2 sides L, R
## Find the mid point of the list
# Assign a left and a right list around the midpoint
# # Then calls recursively on the L & R lists until base case is reached
# After calls the merge function on the Left & Right sides
# 2) create a function that merges them together until len left list and right list < 1
# 3) create a thrid main function that calls merge sort on the array.


def merge_sort(array):
    """recursively splits the array until each item is in it's own list"""

    # check to see if length of array is less than one, if it is return it
    if len(array) <= 1:
        return array

    # find the mid point of the array
    midpoint = int(len(array) // 2)

    # split the list into a left and a right side
    left_list, right_list = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])

    # call the merge function with the L and R sides
    return merge(left_list, right_list)


def merge(left, right):
    """Merges the left and the right sides of the list"""
    # set and empty results list
    result = []

    # set left and right indicies
    left_index = 0
    right_index = 0
    # left.append(9999999999999)
    # right.append(9999999999999)

    # set the while loop to loop through until the length of the left and right lists are less than 1
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def main():
    """ calls the merge sort funciton"""
    array = [5,6,4,3,2,8,19,22]
    print array
    print merge_sort(array)

if __name__ == "__main__":
    import sys

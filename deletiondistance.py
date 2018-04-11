'''
Deletion Distance
The deletion distance of two strings is the minimum number of characters you 
need to delete in the two strings in order to get the same string. For instance, 
the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletion
Distance that returns the deletion distance between them. 

Explain how your function works, and analyze its time and space complexities.

Examples:

input: str1 = "dog", str2 = "frog"
output: 3

input: str1 = "some", str2 = "some"
output: 0

input: str1 = "some", str2 = "thing"
output: 9

input: str1 = "", str2 = ""
output: 0
Constraints:

[input] string str1
[input] string str2
[output] integer

'''
# Create a function that takes in two strings
def del_distance(string1, string2):
    """Takes 2 strings and calculates the number of letters you need to delete to have the words match"""
    
    # set a counter to count the matches
    counter = 0
    # then compare the index of the first string
    for i, s1char in enumerate(string1):
        # to the indicies in the second string until there is a match, if there isn't a match +1
        for j, s2char in enumerate(string2):
        # if there is a match, save the index & move forward to test the next index of the first string. if it doesn't match continue counter +1
            if s1char == s2char:
            # if it does match the first string entirely, add +1 from the second for each index up until the orig match
                # set a pointer at the curent index + 1
                first_match_s1 = i
                first_match_s2 = j

                # now we have a pointer for s1 & s2 when the chars match,
                # we want to compare next char in index 1 to next index 2
                while i < len(string1) - 1 and j < len(string2) - 1:
                    if string1[i + 1] == string2[j + 1]:
                        # this increases the pointer by 1 each match
                        i += 1
                        j += 1

    counter += len(string1[:first_match_s1])
    counter += len(string2[:first_match_s2])
    # counter = len(string1[first_match_s1:i]) + len(string2[first_match_s2:j])

    return counter

print del_distance("dog", "frog")





















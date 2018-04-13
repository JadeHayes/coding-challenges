'''I want to learn some big words so people think I'm smart.

I opened up a dictionary to a page in the middle and started flipping through, 
looking for words I didn't know. I put each word I didn't know at 
increasing indices (?)
in a huge list I created in memory. When I reached the end of the dictionary, 
I started from the beginning and did the same thing until I reached the page I started at.

Now I have a list of words that are mostly alphabetical, 
except they start somewhere in the middle of the alphabet, 
reach the end, and then start from the beginning of the alphabet. 
In other words, this is an alphabetically ordered list that has been "rotated." For example:

  words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

Write a function for finding the index of the
"rotation point," which is where I started working
from the beginning of the dictionary.
This list is huge (there are lots of words I don't know) so we want to be efficient here.'''

# Create a function that takes in a list of words
# create an alpabet dictionary with values of where the letter is in the alphabet

# iterate over the list of words with enumerate
# if the first character of the word has a greater value than the second character (i+1)
# break
# if the value of the current char is less than the next, continue

# FIXME

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]


def rotation_point(words):
    '''takes in a list of words and finds the index of the rotation point'''

    # loop through the list of words
    for i, word in enumerate(words):
        # if the index is not the last index in the list
        if i != len(words) - 1:
            # if the word comes before the next word in the list we
            # found the rotation point
            if word > words[i+1]:
                return words[i+1], "is the rotation point"

print rotation_point(words)

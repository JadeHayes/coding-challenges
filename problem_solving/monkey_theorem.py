# write a function that takes a random char from alph + space
# goal:: "methinks it is like a weasel"
import random

def choice():
    """ choose a rand char """
    # have a string of chars to choose from
    chars = "abcdefghijklmnopqrstuvwxyz "
    ans = ""

    # randomly choose one and add to a list as long as it it less than 27 chars
    while len(ans) < 27:
        # import pdb; pdb.set_trace()
        choice = random.choice(chars)
        ans += choice
    # return the list
    return ans


def ismatch(quote):
    """takes in the random output and matches to goal sentence"""
    # take in a the random output
    # match it to the goal phrase
    # return if it is true or not
    # Check to see if true or false
    goal = "methinks it is like a weasel"
    # return quote == goal
    correctness = 0
    for i in range(len(quote)):
        if quote[i] == goal[i]:
            correctness += 1
    correctness = "%.20f" % correctness
    return float(correctness)/len(goal)


####################################################################
# This needs some work. #FIXME

def score():
    """will repeatedly call and ismatch and choice"""
    # best: the top score of current matches
    best = 0
    # how many times we've been through the while loop
    counter = 0

    # setting the score to the random choice comparison to goal string
    score = ismatch(choice())

    # if the score is less than 1 (100%) add 1 to the counter every iteration.
    # print the best score ever 1000 guesses
    # if the score is better than the best, best is now the new score
    # change the value of score
    while score < 1:
        counter += 1
        if counter % 1000 == 0:
            print "best random choice percent is %s" % (best)
        if score > best:
            best = score
        if counter == 3000:
            return best
        score = ismatch(choice())
    else:
        # if %100 of the letters are correct, we are done
        return "We found a match! in %d tries" % (best)
    # should print out best string generated so far, every 1000 tried

# Description

# You've been given the task of retrieving the top N high scores from players of a video game.

# You need to write the function top_scores(records, n_top)

# where records is a list of lists in the form of

# records = [
#   ["Bob", 100],
#   ["Jane", 120],
#   ["Alice", 10],
#   ["Bob", 110],
#   ["Bob", 10]
# ]
# and n_top is an integer.

# The function should return the top n records, where each user name can appear at most a single time. Records should be in from highest to lowest. Users with the same score should be in alphabetical order.

# >>> top_scores(records, 3)
# [["Jane", 120],["Bob", 110],["Alice", 10]]
# if n_top is negative or 0, the returned value should be an empty list.

# if n_top is greater than the total number of records, you should include as many valid records as possible.


def top_scores(records, n_top):
    scores = {}
    ans = []

    if n_top < 1:
        return []

#     set up a dictionary w/ name & highest score
    for record in records:
        name, score = record[0], record[1]
        if scores.get(name) < score:
            scores[name] = score
        else:
            scores[name] = scores.get(name, score)

# iter items through the dictionary and append each key:val to the list
    for name, high_score in scores.iteritems():
        ans.append([name, high_score])
# sort the list of list with an inline function
    ans = sorted(ans)
    new_ans = sorted(ans, key=lambda ans: ans[1], reverse=True)
    return new_ans[:n_top]  

# sorted(ans, key=lambda inner_lst: inner_lst[1], reverse=True)

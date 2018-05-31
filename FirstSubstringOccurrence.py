def findFirstSubstringOccurrence(s, x):
    j=0
    ans = []

    if not x:
        return -1

    for index, letter in enumerate(s):
        if letter == x[j]:
            ans.append(index)
            if j < len(x) -1:
                j += 1
            elif j == len(x) - 1:
                return ans[0]
        else:
            j = 0
            ans =[]
            if letter == x[j]:
                ans.append(index)
                j += 1
    return -1

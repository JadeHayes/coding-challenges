def get_middle(s):
    ans = ""
    #check to see if the length is odd
    if len(s) % 2 != 0:
#     if odd, divide word by 1/2 len of the word
        letter = len(s)/2
        ans += s[letter]
    else:
# if its even return len/2 floor & ceiling
        letter = (len(s) // 2) - 1
# append the ans to the ans string
        ans += s[letter] + s[letter + 1]
    return ans
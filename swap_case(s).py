def swap_case(s):
#     loop through s
# if char is lower change it to isupper
# if char is upper, change to lower
    ans = ""

    for char in s:
        if char.lower() == char:
            ans += char.upper()
        elif char.upper() == char:
            ans += char.lower()
        else:
            ans += char
    return ans
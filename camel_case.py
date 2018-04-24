def camel_case(string):
    return string.title().replace(" ", "")


def camel_case(string):
    ans = ""
    #create a list by splitting the word at the spaces
    words = string.split(" ")
#     loop through list and add ans to ans string in .title format
    for word in words:
        ans += word.title()
    return ans
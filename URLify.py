# Write a function that changes spaces in a string to %20
def urlify(string):
    """Change the spaces in the URL to %20"""
    url = ""
    for char in string:
        if char == " ":
            url += "%20"
        else:
            url += char
    return url
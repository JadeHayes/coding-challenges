def solve(st):
#     loop over each character in the string in reverse
#  if the character is alpha, add to a temp string
# if it is int, temp string += int * temp string
    temp_string = ""
    
#     loop through the string in reverse order
    for char in st[::-1]:
#     if the current character is alpha
        if char.isalpha():
#         add the char directly to the temp string
            temp_string += char
#     if it isnt, try to int the character
# then multiply it by the temp string we currently have
        try:
            int(char)
            temp_string *= int(char)
# if you cannot "int" it, pass b/c its a "(" or a ")"
        except:
            pass
#       return our temp string reversed
    return temp_string[::-1]


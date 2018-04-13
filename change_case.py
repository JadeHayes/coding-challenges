def change_case(identifier, targetCase):
#     check for specific case in indentifier
        split_lst = []
        ans = ""
        
        # Check to see which type of input the identifier is
        is_camel = any(char.isupper() for char in identifier)
        is_snake = any(char == "_" for char in identifier)
        is_kebab = any(char == "-" for char in identifier)

         # split the identifier according to the input type
        if is_kebab and not is_camel and not is_snake:
            split_lst = identifier.split("-")
        elif is_snake and not is_camel and not is_kebab:
            split_lst = identifier.split("_")
        elif is_camel and not is_kebab and not is_snake:
            for char in identifier:
                if char.isupper():
                    split_lst.append(" ")
                split_lst.append(char)
            split_lst = "".join(split_lst).split(" ")
        elif identifier == "":
            split_lst.append("")
        else:
            return None
            
        # check the target case and join accordingly
        if "camel" == targetCase:
            for word in split_lst:
                if word != split_lst[0]:
                    ans += word.title()
                else:
                    ans += word
        elif "snake" == targetCase:
            split_lst = [word.lower() for word in split_lst]
            ans = "_".join(split_lst).lower()
        elif "kebab" == targetCase:
            ans = "-".join(split_lst).lower()
        else:
            return None

        # return the ans string
        return ans

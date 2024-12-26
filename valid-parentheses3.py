
class Solution:
    def isValid(self, s: str) -> bool:

        left_set = set(["(","{","["]) 
        right_set = set([")","}","]"]) 

        pair_dict = {
            ")":"(",
            "}":"{",
            "]":"[",

            "(":")",
            "{":"}",
            "[":"]",

        }

        stack = []
        for x in s:
            #  print("stack:", stack)
            if stack:
                if x in right_set:
                    if stack[-1]==pair_dict[x]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(x)
            else:
                if x in right_set:
                    return False
                else:
                    stack.append(x)

        if stack:
            return False

        return True



class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)==1:
            return False

        left_set = set(["(","{","["]) 

        pair_dict = {
            ")":"(",
            "}":"{",
            "]":"[",

            "(":")",
            "{":"}",
            "[":"]",


        }

        i = 0
        j = len(s)-1
        while i<j:
            if s[i]==pair_dict[s[i+1]] and (s[i] in left_set):
                i+=2
            elif s[j-1]==pair_dict[s[j]] and (s[j-1] in left_set):
                j-=2
            elif s[i]==pair_dict[s[j]] and (s[i] in left_set):
                i+=1
                j-=1
            else:
                return False

        print("i:", i)
        print("j:",j)



        if i==j:
            return False



        return True



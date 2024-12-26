class Solution:
    def isValid(self, s: str) -> bool:
        left_count = {
            "(":0,
            "{":0,
            "[":0,
        }
        left_set = set(["(","{","["]) 
        # right_set = set([")","}","]"])
        pair_dict = {
            ")":"(",
            "}":"{",
            "]":"[",
        }

        for x in s:
            if x in left_set:
                left_count[x]+=1
            else:
                y = pair_dict[x]
                if left_count[y]<1:
                    return False
                else:
                    left_count[y]-=1
        
        for k,v in left_count.items():
            if v>0:
                return False

        return True
            

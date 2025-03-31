class Solution:
    def isValid(self, s: str) -> bool:
        sym = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        seen = []

        if len(s) % 2 != 0:
            return False

        for i in s:
            if i in sym.keys(): 
                seen.append(i)
            elif i in sym.values():  
                if not seen or sym[seen.pop()] != i: 
                    return False
        return not seen
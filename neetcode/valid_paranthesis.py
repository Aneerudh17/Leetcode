class Solution:
    def isValid(self, s: str) -> bool:
        utils = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        seen = []
        for i in s:
            if i in utils.keys():
                seen.append(i)
            elif i in utils.values():
                if not seen or utils[seen.pop()] != i:
                    return False
        return not seen       
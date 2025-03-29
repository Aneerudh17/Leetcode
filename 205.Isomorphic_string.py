class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_index = {}
        t_index = {}

        for i in range(len(s)):
            if s[i] not in s_index:
                s_index[s[i]] = i
            
            if t[i] not in t_index:
                t_index[t[i]] = i

            if s_index[s[i]] != t_index[t[i]] :
                return False
        return True
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p :
            return not s
        
        first_match = (len(s)>0) and (s[0] == p[0] or p[0] == ".")

        if len(p) >= 2 and p[1] == "*":
            #either ignore the first character from p and continue with the rest.
            #if the first character mmatches, check from s[1]
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            #if there are no * sign then just check if both s and p has same characters.
            return first_match and self.isMatch(s[1:], p[1:])
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_len = math.gcd(len(str1),len(str2))

        candidate = str1[:gcd_len]
        if candidate * (len(str1) // gcd_len) == str1 and candidate * (len(str2) // gcd_len) == str2:
            return candidate
        else:
            return ""
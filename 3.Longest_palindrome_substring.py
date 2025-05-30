class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        longest = ""

        for i in range(len(s)):
            for j in range(i + max_len, len(s)):
                substr = s[i:j+1]
                if substr == substr[::-1]:  # Check if palindrome
                    if len(substr) > max_len:
                        max_len = len(substr)
                        longest = substr

        return longest
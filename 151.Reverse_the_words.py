class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split().reverse()
        res = []

        for i in range(len(words)):
            res.append(words[i])

        return "".join(res)
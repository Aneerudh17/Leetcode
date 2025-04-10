class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        words = [i for i in s.split()]
        for i in words:
            count += 1
        return count
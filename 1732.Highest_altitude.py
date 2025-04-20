class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = highest = 0
        for i in gain:
            current += i
            highest = max(highest,current)
        return highest
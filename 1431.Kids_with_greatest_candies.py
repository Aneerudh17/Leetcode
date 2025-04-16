class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        result = []
        for c in candies:
            result.append(c + extraCandies >= greatest)
        return result
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = [] #seen set to track the elements
        for num in nums:
            if nums in seen:
                return True #if num is present in seen, then the number is duplicated so return true
            seen.append(num) #if num is not present then add the number to the seen set.
        return False #if it doesnt satisfy any of the above condition then return false
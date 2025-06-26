class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        #list comprehension to retrieve positive numbers from the list
        nums = [n for n in nums if n > 0]

        #sorting the list 
        nums.sort()
        
        #the target is always 1 cuz it the lowest possible positive number
        target = 1

        for n in nums:
            if n == target:
                target += 1
            elif n > target:
                return target
        return target
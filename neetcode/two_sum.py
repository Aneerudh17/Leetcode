class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        comp = {}

        n = len(nums)

        for i in range(n):

            #find the complement
            complement = target - nums[i]
            #check if the complement is present in the hash or not
            if complement in comp:
                return [comp[complement],i]
        #add the numbers to the hash after visiting them
        comp[nums[i]] = i
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = result = nums[0]
        for i in range(1,len(nums)):
            maximum = max(nums[i],maximum + nums[i])
            result = max(result,maximum)
        return result
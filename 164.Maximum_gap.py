class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        gap = 0
        if len(nums) == 1:
            return 0
        else:
            for i in range(1,len(nums)):
                gap = max(gap,nums[i]-nums[i-1])
            return gap
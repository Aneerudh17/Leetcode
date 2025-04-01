class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]

        start,end = -1,-1
        
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                break

        for i in range(len(nums)-1,-1,-1):
            if nums[i] == target:
                end = i
                break
            
        return [start,end]
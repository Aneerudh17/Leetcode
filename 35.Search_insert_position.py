class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        else:
            i = 0
            j = 1

            while j < len(nums):
                if nums[i] == target:
                    return i
                
                if nums[i] <= target < nums[j]:
                    return j
                
                i += 1
                j += 1 
            if target == nums[-1]:
                return len(nums) - 1  
            return len(nums) 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = numms[i]
                j += 1
        return j
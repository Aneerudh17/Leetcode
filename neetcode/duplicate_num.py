class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_arr = []
        for i in nums:
            if i not in new_arr:
                new_arr.append(i)
        return new_arr
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)

        if n == 1:
            return True

        if n == 2:
            return True

        for i in range(n-1):
            if nums[i] + nums[i + 1] >= m:
                return True

        return False

'''
js solution:
/**
 * @param {number[]} nums
 * @param {number} m
 * @return {boolean}
 */
var canSplitArray = function(nums, m) {
    let n = nums.length;

    if (n === 1){
        return true;
    }

    if (n === 2){
        return true;
    }

    for (let i = 0; i < n-1; i++){
        if (nums[i] + nums[i + 1] >= m){
            return true;
        }
    }
    return false;
'''
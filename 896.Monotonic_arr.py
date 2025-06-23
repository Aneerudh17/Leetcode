class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        for i in range(1,n):
            if nums[i] < nums[i-1]:
                break
            
            if i == n-1:
                return True
        
        for i in range(1,n):
            if nums[i]> nums[i-1]:
                break
            
            if i == n-1:
                return True
            
        return False
    
'''
js solution:
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMonotonic = function(nums) {
    const n = nums.length;
        if (n === 1) {
            return true;
        }
        for (let i = 1; i < n; i++) {
            if (nums[i] < nums[i - 1]) {
                break;
            }
            if (i === n - 1) {
                return true;
            }
        }
        for (let i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                break;
            }
            if (i === n - 1) {
                return true;
            }
        }
        return false;
    }
'''
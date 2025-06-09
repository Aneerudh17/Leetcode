#classic binary search approach:
'''
javascript sol:
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let left = 0;
    let right = nums.length-1;

    while(left<right){
        const mid = Math.floor((left + right)/2);

        if (nums[mid] <= nums[right]){
            right = mid;
        }
        else{
            left = mid + 1;
        }

    }
    return nums[left];
    
};
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]
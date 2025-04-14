class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == max(nums):
                return i
            
'''
optional rust solution:
impl Solution {
    pub fn find_peak_element(nums: Vec<i32>) -> i32 {
        for i in 0..nums.len() {
            if nums[i] == *nums.iter().max().unwrap() {
                return i as i32;
            }
        }
        -1
    }
}
'''
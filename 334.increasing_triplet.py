class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
    
'''
rust solution:
impl Solution {
    pub fn increasing_triplet(nums: Vec<i32>) -> bool {
        let mut first = i32::MAX;
        let mut second = i32::MAX;

        for n in nums{
            if n <= first{
                first = n;
            }
            else if n <= second{
                second = n;
            }
            else{
                return true;
            }

        }
        return false;
        
    }
}
'''
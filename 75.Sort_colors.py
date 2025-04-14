class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = count_1 = count_2 = 0
        for num in nums:
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
            else :
                count_2 += 1

        index = 0
        for i in range(count_0):
            nums[index] = 0
            index += 1
        for i in range(count_1):
            nums[index] = 1
            index += 1
        for i in range(count_2):
            nums[index] = 2
            index += 1
        return nums
    
'''
optional rust solution
impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let mut count_0 = 0;
        let mut count_1 = 0;
        let mut count_2 = 0;

        for &i in nums.iter(){
            if i == 0{
                count_0 += 1;
            }
            else if i == 1{
                count_1 += 1;
            }
            else{
                count_2 += 1;
            }
        }
        let mut index = 0;
        for i in 0..count_0{
            nums[index] = 0;
            index = index + 1;
        }
        for i in 0..count_1{
            nums[index] = 1;
            index = index + 1;
        }
        for i in 0..count_2{
            nums[index] = 2;
            index = index+1;
        }
    }
}
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums)-2): #reducing two values for left and right pointers
            left , right = i+1, len(nums)-1 #placing the pointers

            while left<right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target: #since the nums list is sorted, you move by one item to the right to increase the sum
                    left += 1
                
                elif current_sum > target: #vice versa
                    right -= 1
                
                else:
                    return current_sum
        return closest_sum
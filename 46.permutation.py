class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        result = []

        for i in range(len(nums)):
            current = nums[i]
            remaining = nums[:i] + nums[i+1:]

            for p in self.permute(remaining):
                result.append([current]+p)
        return result
    
'''
how to solve :
pick a number from the range
pair it with another number
add the remaining number and append to the result list
'''

'''
current = nums[i] #pick the current number
remaining = nums[:i] + nums[i+1:] # picks all the numbers other than the number we picked

for p in self.permute(remaining) # again breaks the smaller list we got into smaller list untill there is no more permutation
result.append([current]+p) #adds it to our current number
'''
'''
js solution:
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    if(nums.length === 0) return [[]];
    let result = [];
    for (let i = 0; i < nums.length; i++){
        let current = nums[i];
        let remaining = nums.slice(0,i).concat(nums.slice(i+1));
        let perms = permute(remaining);
        for (let perm of perms){
            result.push([current].concat(perm));
        }
    }
    return result;
};
'''
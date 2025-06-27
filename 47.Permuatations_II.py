class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        result = []

        for i in range(len(nums)):
            #choosing a number from the list sequentially
            current = nums[i]
            #slicing the remaining numbers from the list
            remaining = nums[:i] + nums[i+1:]

            for p in self.permuteUnique(remaining):
                #checking if the list is there in the result or not before appending
                if ([current] + p) not in result:
                    #if not then append, else skip
                    result.append([current]+p)
            
        return result
#not the most efficient solutiton but easier to understand.


'''
js solution
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    if (nums.length === 0){
        return [[]];
    }
    
    let result = [];

    for(let i = 0; i < nums.length; i++){
        let current = nums[i];
        let remaining = nums.slice(0,i).concat(nums.slice(i+1));
        let perms = permuteUnique(remaining);
        for (perm of perms){
            if (!perm in result){
                result.push([current].concat(perm));
            }
        }
    }
    return result;
};
'''
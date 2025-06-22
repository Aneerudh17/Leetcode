class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)& set(nums2))
    

'''
js solution:
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    const set1 = new Set(nums1);
    const set2 = new Set(nums2);
    const result = [];

    for (let num of set1) {
        if (set2.has(num)) {
            result.push(num);
        }
    }

    return result;
    
};
'''
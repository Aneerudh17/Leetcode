class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1

        return n - left
    
'''
js solution
/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    let n = citations.length;
    let left = 0;
    let right = n -1;
    while (left <= right){
        let mid = Math.floor((left+right)/2);

        if (citations[mid]>= n - mid){
            right = mid -1;
        }
        else{
            left = mid + 1;
        }
    }
    return n - left
    
};
'''
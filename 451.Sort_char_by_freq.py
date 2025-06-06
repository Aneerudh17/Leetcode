class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        def get_frequency(item):
            return item[-1]
        
        freq = Counter(s)

        sorted_char = sorted(freq.items(),key=get_frequency,reverse=True)

        result = ''.join(char * count for char, count in sorted_char)

        return result
    
'''
javascript solution:
/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    const freqMap = new Map();
    for (let char of s) {
        freqMap.set(char, (freqMap.get(char) || 0) + 1);
    }
    const sortedChars = Array.from(freqMap.entries()).sort((a, b) => b[1] - a[1]);
    let result = '';
    for (let [char, count] of sortedChars) {
        result += char.repeat(count);
    }
    return result;
    
};
'''
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for i in arr:
            if i in freq :
                freq[i] += 1
            if i not in freq:
                freq[i] = 1
        occurance = freq.values()
        return len(occurance) == len(set(occurance))
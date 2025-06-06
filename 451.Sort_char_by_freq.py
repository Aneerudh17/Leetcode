class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        def get_frequency(item):
            return item[-1]
        
        freq = Counter(s)

        sorted_char = sorted(freq.items(),key=get_frequency,reverse=True)

        result = ''.join(char * count for char, count in sorted_char)

        return result
    

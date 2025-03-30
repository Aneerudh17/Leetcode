class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_list = list(pattern)
        words = list(s.split())
        
        # If lengths don't match, immediately return False
        if len(pattern) != len(words):
            return False
        
        dict1 = {}
        for i in range(len(pattern)):
            if pattern_list[i] in dict1:
                if dict1[pattern_list[i]] != words[i]:
                    return False
            else:
                # Check if the word is already mapped to another pattern character
                if words[i] in dict1.values():
                    return False
                dict1[pattern_list[i]] = words[i]
        
        return True

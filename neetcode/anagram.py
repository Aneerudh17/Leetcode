class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}

        #goal is to check if the count of each character in both strings match

        for char in s:
            #add each char from the string s to the hash counter while initialising it to 0
            counter[char] = counter.get(char,0) + 1

        for char in t:
            #now check if the char is in the counter or not
            if char not in counter or counter[char] == 0:
                #if not present then return false
                return False
            #if present reduce the counter by 1
            counter[char] -= 1
        #if every condition satisfies then return true
        return True
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        max_length = max(len(word1),len(word2))

        for i in range(max_length):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]

        return result
    
'''
alternative rust solutions:
impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        use std::cmp::max;
        let mut result = String::new();

        let chars1: Vec<char> = word1.chars().collect();
        let chars2: Vec<char> = word2.chars().collect();
        
        let max_length = max(chars1.len(), chars2.len());

        let mut max_length = max(chars1.len(),chars2.len());
        for i in 0..max_length{
            if i < chars1.len(){
                result.push(chars1[i]);
            }
            if i < chars2.len(){
                result.push(chars2[i]);
            }
        }
        return result;

'''
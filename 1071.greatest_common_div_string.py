class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_len = math.gcd(len(str1),len(str2))

        candidate = str1[:gcd_len]
        if candidate * (len(str1) // gcd_len) == str1 and candidate * (len(str2) // gcd_len) == str2:
            return candidate
        else:
            return ""
        
'''
rust solution:
impl Solution {
    pub fn gcd_of_strings(str1: String, str2: String) -> String {
        fn gcd(mut a: usize, mut b: usize) -> usize {
            while b != 0 {
                let temp = b;
                b = a % b;
                a = temp;
            }
            a
        }

        let len1 = str1.len();
        let len2 = str2.len();
        let gcd_len = gcd(len1, len2);
        let candidate = &str1[..gcd_len];

        if candidate.repeat(len1 / gcd_len) == str1 && candidate.repeat(len2 / gcd_len) == str2 {
            candidate.to_string()
        } else {
            "".to_string()
        }
    }
}
'''
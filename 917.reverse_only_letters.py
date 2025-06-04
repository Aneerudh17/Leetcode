class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        s = list(s)
        i = 0
        j = len(s)-1

        while i< j:
            if s[i] not in chars:
                i += 1
            elif s[j] not in chars:
                j -= 1
            
            else:
                s[i] , s[j] = s[j] , s[i]
                i += 1
                j -=1

        return "".join(s)
    
'''
javascript solution:
/**
 * @param {string} s
 * @return {string}
 */
var reverseOnlyLetters = function(s) {
    const isLetter = (char) => /[a-zA-Z]/.test(char);
        let arr = s.split('');
        let i = 0;
        let j = arr.length - 1;

        while (i < j) {
            if (!isLetter(arr[i])) {
                i++;
            } else if (!isLetter(arr[j])) {
                j--;
            } else {
                [arr[i], arr[j]] = [arr[j], arr[i]];
                i++;
                j--;
            }
        }

        return arr.join('');
    }
  
'''
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        #if postive sign = 1 else -1
        sign = 1
        #initialising a pointer
        i = 0
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '+' or ch == '-':
                result += sign * num
                num = 0
                sign = 1 if ch == '+' else -1

            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
                
            elif ch == ')':
                result += sign * num
                num = 0
                prevSign = stack.pop()
                prevRes = stack.pop()
                result = prevRes + prevSign * result
            i += 1  
        if num:
            result += sign * num
        return result
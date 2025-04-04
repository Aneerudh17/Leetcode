class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n < 0 :
            n = -n
            while n>0:
                result *= x
                n -=1
            return 1/result
        else:
            while n>0:
                result *=x
                n-=1
            return result
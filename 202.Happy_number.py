class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n!= 1 and n not in seen:
            seen.add(n)
            digits = [int(d) for d in str(n)]
            result = 0

            for digit in digits:
                result += digit ** 2
            n = result

        return n == 1
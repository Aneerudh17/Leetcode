class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for item in s:
            if item == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        return ''.join(stack)
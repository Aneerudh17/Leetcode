class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for choice in operations:
            if choice == "C":
                stack.pop()
            elif choice == "D":
                stack.append(stack[-1]*2)
            elif choice == "+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(choice))
        return sum(stack)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x not in {"+", "-", "*", "/"}:
                stack.append(x)
            if x == "+":
                if stack:
                    l = int(stack.pop())
                if stack:
                    r = int(stack.pop())
                stack.append(l + r)
            if x == "-":
                if stack:
                    r = int(stack.pop())
                if stack:
                    l = int(stack.pop())
                stack.append(l - r)
            if x == "*":
                if stack:
                    l = int(stack.pop())
                if stack:
                    r = int(stack.pop())
                stack.append(l * r)
            if x == "/":
                if stack:
                    r = int(stack.pop())
                if stack:
                    l = int(stack.pop())
                stack.append(int(l / r))
        return int(stack[-1])

        
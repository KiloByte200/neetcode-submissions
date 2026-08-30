class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for cand in tokens:
            if cand not in {"+", "-", "*", "/"}:
                stack.append(int(cand))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if cand == "+":
                    stack.append(num1 + num2)
                elif cand == "-":
                    stack.append(num1 - num2)
                elif cand == "*":
                    stack.append(num1 * num2)
                elif cand == "/":
                    stack.append(int(num1 / num2))
        return stack.pop()

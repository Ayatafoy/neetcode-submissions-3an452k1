class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        operators = set(["+", "-", "*", "/"])
        result = 0
        for token in tokens:
            if token in operators:
                print(stack)
                first = int(stack.pop())
                second = int(stack.pop())
                print(first)
                print(second)
                if token == "+":
                    result = first + second
                elif token == "-":
                    result = second - first
                elif token == "*":
                    result = first * second
                elif token == "/":
                    result = int(second / first)
                stack.append(result)
            else:
                stack.append(token)
        return result
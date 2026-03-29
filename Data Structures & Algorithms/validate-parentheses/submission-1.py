class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        for c in s:
            if c in lookup.values():
                stack.append(c)
            else:
                if len(stack) == 0 or lookup[c] != stack.pop():
                    return False
        if len(stack) > 0:
            return False
        return True
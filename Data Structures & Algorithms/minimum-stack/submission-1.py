class MinStack:

    def __init__(self):
        self.min_values = []
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.min_values) == 0 or self.min_values[-1] >= val:
            self.min_values.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        top_value = self.top()
        if top_value == self.min_values[-1]:
            self.min_values.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]
        

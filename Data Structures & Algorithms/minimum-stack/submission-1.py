class MinStack:
    stack = []

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        import sys
        min_val = sys.float_info.max   
        for i in self.stack:
            min_val = min(min_val, i)
        return min_val

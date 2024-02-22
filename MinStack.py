class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack == None:
            return None
        else:
            temp = self.stack[-1]
            self.stack = self.stack[:-1]
            return temp

    def top(self) -> int:
        if self.stack == None:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack:

    def __init__(self):
        self.items = []  # it will be having list in it [val , minimumValTillNow]

    def push(self, val: int) -> None:
        if len(self.items) == 0:  # the value coming is the min
            self.items.append([val, val])
        else:  # items not null
            mini = min(self.items[-1][1], val)
            self.items.append([val, mini])

    def pop(self) -> None:
        if len(self.items) != 0:
            self.items.pop()

    def top(self) -> int:
        if len(self.items) != 0:
            return self.items[-1][0]
        return None

    def getMin(self) -> int:
        if len(self.items) != 0:
            return self.items[-1][1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

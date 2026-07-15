class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while self.stack1:  # palce all elem from s1 to s2
            self.stack2.append(self.stack1.pop())
        # now when s1 empty add the upcoming elm to s1
        self.stack1.append(x)
        # now again remove all elem from s2 and add to s1
        while self.stack2:  # palce all elem from s2 to s1
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        # top mosrt of s1
        if len(self.stack1) == 0:
            return None
        return self.stack1.pop()

    def peek(self) -> int:
        if len(self.stack1) == 0:
            return None
        return self.stack1[-1]

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

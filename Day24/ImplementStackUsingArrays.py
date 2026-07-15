class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.arr = []
        self.n = n
    
    def isEmpty(self):
        # Check if stack is empty
        if len(self.arr)==0:
            return True
        return False
    
    def isFull(self):
        # Check if stack is full
        if self.n == len(self.arr):
            return True
        return False
    
    def push(self, x):
        # Insert x at the top of the stack
        if self.n != len(self.arr):
            self.arr.append(x)
            
    def pop(self):
        # Removes an element from the top of the stack
        if len(self.arr)!=0:
            return self.arr.pop()

    def peek(self):
        # Returns the top element of the stack
        if len(self.arr)!=0:
            return self.arr[-1]
        return -1
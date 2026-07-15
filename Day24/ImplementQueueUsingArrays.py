from collections import deque
class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.n = n
        self.que = deque([])
    
    def isEmpty(self):
        # Check if queue is empty
        if len(self.que)==0:
            return True
        return False

    
    def isFull(self):
        # Check if queue is full
        if len(self.que)==self.n:
            return True
        return False

    
    def enqueue(self, x):
        # Enqueue
        if len(self.que)!=self.n:
            self.que.append(x)

    
    def dequeue(self):
        # Dequeue
        if len(self.que)!=0:
            self.que.popleft()

    
    def getFront(self):
        # Get front element
        if len(self.que)!=0:
            return self.que[0]
        
        return -1
       
    
    def getRear(self):
        # Get rear element 
        if len(self.que)!=0:
            return self.que[-1]
        
        return -1
        
        
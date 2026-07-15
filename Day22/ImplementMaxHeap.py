import heapq


class maxHeap:

    def __init__(self):
        self.heap = []

    def push(self, x: int):
        heapq.heappush(self.heap, -x)

    def pop(self):
        if self.heap:
            heapq.heappop(self.heap)

    def peek(self) -> int:
        if not self.heap:
            return -1
        return -self.heap[0]

    def size(self) -> int:
        return len(self.heap)
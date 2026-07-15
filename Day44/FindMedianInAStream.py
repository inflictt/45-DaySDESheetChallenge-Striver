class MedianFinder:

    def __init__(self):
        self.arr = []  # this will value and currmedia till here

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        # is even then mid 2 elem ka avg
        # if odd directly n//2
        self.arr = sorted(self.arr)

        if len(self.arr) % 2 != 0:  # odd
            return self.arr[len(self.arr) // 2]
        else:  # even
            n = len(self.arr)
            mid1 = self.arr[n // 2 - 1]
            mid2 = self.arr[n // 2]
            return (mid1 + mid2) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

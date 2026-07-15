class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums  # lsit made
        self.target = k

    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream = sorted(self.stream, reverse=True)
        return self.stream[self.target - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# ecxample - [3, [4, 5, 8, 2]
# so in thus k is 3 and nums = [4, 5, 8, 2] right
# so on add4 is added
# add functino task si to add the elm into stram adn return k th larfest frmo pool so far seen

class StockSpanner:

    def __init__(self):
        self.stack = []  # (price, span)

    def next(self, price: int) -> int:
        span = 1
        # we can update then span of curr when top val is less than upcom value and we will pop it until top becomes greater then current or stack goes empty
        while self.stack and self.stack[-1][0] <= price:  # topVal<price Allow update
            e = self.stack.pop()
            prevSpan = e[1]
            span += prevSpan

        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

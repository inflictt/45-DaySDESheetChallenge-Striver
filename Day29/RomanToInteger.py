class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)  # LVIII = 5 totl
        # pos = #left most
        letters = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        arr = []
        for i in range(n):
            ch = s[i]
            arr.append(letters[ch])
        # MCMIV
        # arr = [1000, 100, 1000, 1, 5] i. at 5
        total = arr[-1]
        prev = arr[-1]
        for i in range(n - 2, -1, -1):
            curr = arr[i]  #
            if prev == curr:  # do nothing fine
                total = total + curr
            elif prev > curr:
                total = total - curr
            else:
                total = total + curr
            prev = curr
        return total

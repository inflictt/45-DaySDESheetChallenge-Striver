class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()

        low = 1
        high = stalls[-1] - stalls[0]

        while low <= high:
            mid = (low + high) // 2

            cows = 1
            last = stalls[0]

            for i in range(1, len(stalls)):
                if stalls[i] - last >= mid:
                    cows += 1
                    last = stalls[i]

            if cows >= k:
                low = mid + 1
            else:
                high = mid - 1

        return high
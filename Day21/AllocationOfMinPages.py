class Solution:
    def findPages(self, arr, k):
        n = len(arr)
        if k > n:
            return -1
        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid = (low + high) // 2
            students = 1
            pages = 0
            for book in arr:
                if pages + book <= mid:
                    pages += book
                else:
                    students += 1
                    pages = book
            if students <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low
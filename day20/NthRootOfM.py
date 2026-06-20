class Solution:
    def nthRoot(self, n, m):
       # code here
        if m == 0:
            return 0
        low, high = 1, m
        
        while low <= high:
            mid = (low + high) // 2
            val = mid ** n
        
            if val == m:
                return mid
            elif val < m:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
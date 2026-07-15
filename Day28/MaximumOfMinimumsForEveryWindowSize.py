class Solution:
    def maxOfMins(self, arr):
       # code here
        n = len(arr)
        # Next Smaller Element
        nse = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)

        # Previous Smller elem
        pse = [-1] * n
        stack = []
        for i in range(0, n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)
        ans = [0]*(n+1)
        for i in range(n):
            length = nse[i] - pse[i] - 1
            ans[length] = max(ans[length], arr[i])
        for i in range(n - 1, 0, -1):
            ans[i] = max(ans[i], ans[i + 1])
        return ans[1:]
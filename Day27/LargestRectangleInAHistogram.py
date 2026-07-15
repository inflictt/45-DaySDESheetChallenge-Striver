class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # Next Smaller Element
        nse = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)

        # Previous Smller elem
        pse = [-1] * n
        stack = []
        for i in range(0, n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)

        maxArea = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = heights[i] * width
            maxArea = max(maxArea, area)

        return maxArea

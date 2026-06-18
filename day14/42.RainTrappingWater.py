class Solution:
    def trap(self, height: List[int]) -> int:
        # get the left and right to each index elem
        # from thet form the height at index and then calc area and then update the total
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        leftMax[0] = height[0]
        rightMax[n-1] = height[n-1]
        for i in range(1,n):
            curr = height[i]
            leftMax[i] = max(leftMax[i-1],curr)
        for i in range(n-2,-1,-1):
            curr = height[i]
            rightMax[i] = max(rightMax[i+1],curr)
        total = 0
        # get the curr height fixed and remove the currr building ht and then find the area
        for i in range(n):
            lmx = leftMax[i]
            rmx = rightMax[i]
            ht = min(lmx,rmx)
            area = (ht - height[i]) * 1
            total+=area
        return total

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # using a deque
        n = len(nums)
        que = deque([])
        ans = []
        for i in range(n):
            index = i
            if len(que) == 0:  # empty que add the index irrespectively
                que.append(index)
            else:
                # 1. Remove expired indices
                if que and que[0] <= i - k:
                    que.popleft()
                # 2. Remove smaller elements
                while que and nums[que[-1]] <= nums[i]:
                    que.pop()
                # 3. Add current index
                que.append(i)
            if i >= k - 1:
                ans.append(nums[que[0]])
        return ans

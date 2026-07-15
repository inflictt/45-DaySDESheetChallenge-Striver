import heapq 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # solving via heap min heap tkaing k grops in the arr/heap first tehn iterating thre array completlteyt and pusshing if any big elem found in the arr
        arr = []
        for i in range(k):
            heapq.heappush(arr,nums[i])
        # array hai k elem now 
        for i in range(k,len(nums)):
            if arr[0]<nums[i]:
                heapq.heappop(arr)
                heapq.heappush(arr,nums[i])
        # return top elem,
        return arr[0]

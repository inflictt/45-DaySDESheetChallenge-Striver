import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []#min heap on frquency
        # if heap size > k we pop as we need upto k only
        for num in (freq):
            # number , occur = num , freq[num]
            pair = [freq[num],num]
            heapq.heappush(heap,pair)
            if len(heap)>k:
                heapq.heappop(heap)
        ans = []
        for i in range(len(heap)):
            e = heapq.heappop(heap)#got my answer
            ans.append(e[1])
        return ans
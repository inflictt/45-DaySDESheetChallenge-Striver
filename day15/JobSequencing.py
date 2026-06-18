import heapq

class Solution:
    def jobSequencing(self, deadline, profit):
        # lets first sort our array in terms of deadline
        arr = [(deadline[i], profit[i]) for i in range(len(deadline))]
        arr.sort()
        priorQ = []
        for i in range(len(arr)):

            if len(priorQ) < arr[i][0]:
                heapq.heappush(priorQ, arr[i][1])
            else:
                # replace only if current profit is better
                if priorQ[0] < arr[i][1]:
                    heapq.heappop(priorQ)
                    heapq.heappush(priorQ, arr[i][1])

        return [len(priorQ), sum(priorQ)]
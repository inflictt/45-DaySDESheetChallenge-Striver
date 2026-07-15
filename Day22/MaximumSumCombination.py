class Solution:
    def topKSumPairs(self, a, b, k):
        a.sort(reverse=True)
        b.sort(reverse=True)

        arr = []
        seenSet = set()
        heapq.heappush(arr, (-(a[0] + b[0]), 0, 0))
        seenSet.add((0, 0))
        ans = []
        while k and arr:
            total, i, j = heapq.heappop(arr)

            ans.append(-total) #so we stored the largest sum in the ans array 
    #now just 2 vcheck i+1 , j and i , j+1 so we will check if not seen already and 
    # push totoal and indexs 
            if i + 1 < len(a) and (i + 1, j) not in seenSet:
                heapq.heappush(arr,(-(a[i + 1] + b[j]), i + 1, j))
                seenSet.add((i + 1, j))

            if j + 1 < len(b) and (i, j + 1) not in seenSet:
                heapq.heappush(arr,(-(a[i] + b[j + 1]), i, j + 1))
                seenSet.add((i, j + 1))

            k -= 1

        return ans
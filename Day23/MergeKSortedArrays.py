import heapq
class Solution:
    def mergeArrays(self, mat):
        n = len(mat)
        heap = []
        # putting first element of every row
        for i in range(n):
            heapq.heappush(heap, (mat[i][0], i, 0))
        ans = []
        # itrr heap
        while heap:
            val, row, col = heapq.heappop(heap)
            ans.append(val)
            # Push next element from same row
            if col + 1 < len(mat[row]):
                heapq.heappush(heap,(mat[row][col + 1], row, col + 1) )
# did col+1 as thats my j ptr moving up in terms of value index in arr
        return ans
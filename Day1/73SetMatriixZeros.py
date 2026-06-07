from collections import deque
import copy

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        que = deque()

        # store all positions having 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    que.append((r, c))

        ans = copy.deepcopy(matrix)

        # for every stored zero
        for i in range(len(que)):
            r,c = que.popleft()#gave vals like[[1,1]] = 1,1 now in r,c respect.

            # make rows 0 here for now row = 1 from[[1,1]]
            for k in range(cols):#row fixed cols to be changed
                ans[r][k] = 0
            for j in range(rows):#as col si fixed for this
                ans[j][c] = 0 
            
        matrix[:] = ans
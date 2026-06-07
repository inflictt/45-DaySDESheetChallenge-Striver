class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # core idea is transpose and then reverse
        n = rows = len(matrix)
        cols = len(matrix[0])
        vis = [[0 for c in range(cols)]for r in range(rows)]
        for r in range(rows):
            for c in range(cols):
                #  r to c and c to r and none of them to be done rtwice
                if vis[r][c]==0 :
                    matrix[r][c] , matrix[c][r] = matrix[c][r] , matrix[r][c]
                    vis[r][c]=1 
                    vis[c][r]=1
        for row in matrix:
            row.reverse()
        return matrix
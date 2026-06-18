class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # brute 
        def isSafe(row,col,board,ans,n):
            # top left back diag i-1 and j -1
            copyRow , copyCol =  row, col
            while row>=0 and col>=0:
                if board[row][col]=="Q" : #means queen the toh return false now
                    return False
                row-=1
                col-=1
            # now check just horizontally 
            row , col = copyRow, copyCol
            while row>=0 and col>=0:
                if board[row][col]=="Q" : #means queen the toh return false now
                    return False
                col-=1
            # now check just bottom left diagonally 
            row , col = copyRow, copyCol
            while row<n and col>=0:
                if board[row][col]=="Q" : #means queen the toh return false now
                    return False
                row+=1
                col-=1
            return True
        
        def solve(col,board,ans,n):
            if col == n :
                # store and return
                ans.append(["".join(row) for row in board])
                return 
            for row in range(n):#checking every row
                if isSafe(row,col,board,ans,n):
                    board[row][col] = "Q"
                    solve(col+1, board, ans, n)
                    board[row][col] = "."
        ans = []
        board = [["."] * n for _ in range(n)]
        solve(0,board,ans,n)
        return ans
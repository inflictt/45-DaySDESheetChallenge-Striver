class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # def isValid(board, i, j, d):
        #     for x in range(9):
        #         if board[x][j] == d:  # col check
        #             return False
        #         if board[i][x] == d:  # row check
        #             return False
        #     # box check now
        #     start_i = (i // 3) * 3
        #     start_j = (j // 3) * 3
        #     for a in range(3):
        #         for b in range(3):
        #             if board[start_i + a][start_j + b] == d:
        #                 return False
        #     return True
        def isValid(board, i, j, d):
            start_i = (i // 3) * 3
            start_j = (j // 3) * 3
            for x in range(9):
                # row
                if board[i][x] == d:
                    return False
                # col
                if board[x][j] == d:
                    return False
                # box
                r = start_i + x // 3
                c = start_j + x % 3
                if board[r][c] == d:
                    return False
            return True

        def solve(board):
            digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":  # means we can place some number here
                        for d in digits:
                            if isValid(board, i, j, d):  # then we can place then explore
                                board[i][j] = d
                                if solve(board) == True:
                                    return True
                                board[i][j] = "."  # undo
                        return False  # means hum kuch ni daal paaye toh piche jaake ye wapis check krega issue ko
            return True  # all cells were filled
        solve(board)
        # brute hits tle 6/8 tc passed 
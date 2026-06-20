class Solution:
    def ratInMaze(self, maze):
        # code here
        def dfs(row,col,i,j,maze,ans,vis,string):
            
            if not (i>=0 and j>=0 and i<row and j< col): return
            if maze[i][j]==0: return    
            if i==row-1 and j==col-1 :
                ans.append(string)
                return 
            if vis[i][j]==1: return 
            
        
            vis[i][j] = 1
            dfs(row,col,i-1,j,maze,ans,vis,string+"U")
            dfs(row,col,i,j+1,maze,ans,vis,string+"R")
            dfs(row,col,i+1,j,maze,ans,vis,string+"D")
            dfs(row,col,i,j-1,maze,ans,vis,string+"L")
            vis[i][j] = 0
            
        row = n = len(maze)
        col = len(maze[0])
        vis = [[0 for _ in range(col)]for k in range(row)]
        ans , string = [] , ""
        # for i in range(row):
        #     for j in range(col):
        dfs(row,col,0,0,maze,ans,vis,string)
        ans.sort()
        return ans
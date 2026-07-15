class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows = len(image)
        cols = len(image[0])
        q = deque([(sr,sc)])
        ic = image[sr][sc] #this istthe initial col
        myarr = deepcopy(image)#the arr which il be udpating nd returning as final answer
        vis = [[-1 for _ in range(cols)] for _ in range(rows)]#this be tracking up my moves 
        vis[sr][sc] = 1
        
        while q :
            i,j = q.popleft()#give me the i and j 
            myarr[i][j] = color#rang fill krdo aur phir q mai kya append hoga chekc that
            vis[i][j] = 1
            # dirs = [top,right,btm,left]
            dirs = [(-1,0),(0,1) , (1,0),(0,-1)]
            for x ,y in dirs :
                new_i = x+i
                new_j = y+j

            # now check these bounds
          
                if new_i>=rows or new_j>=cols or new_i<0 or new_j<0:  # check pehele to color k barabar to nhi
                    continue

                # conti if pre vis
                if vis[new_i][new_j]==1:
                    continue
                #check ki woh base color k barabar h ki nhi if not return/continue
                if image[new_i][new_j] != ic:
                    continue
                vis[new_i][new_j] =1
                q.append([new_i,new_j])
        return myarr
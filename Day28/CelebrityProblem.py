class Solution:
    def celebrity(self, mat):
        # code here
        stack = []
        n = len(mat[0])#no of peeps for celleb vacancy
        
        for k in range(n):
            stack.append(k)
        while len(stack)>1:
            i = stack.pop() 
            j = stack.pop()
            if mat[i][j]==0:#means i dont know j so i possbile celeb but j cantbe
                stack.append(i)
            else:
                stack.append(j)
        celeb= stack.pop() #the possbiel celev is top of stack as the only one left
        
        for i in range(n):
            if i==celeb:continue
            if mat[i][celeb] == 0: #mtlb koi ek esa aajaye jo ni jaanta ho isko
                return -1
            elif  mat[celeb][i] == 1: #koi esa jisko ye jaanta ho
                return -1
        return celeb
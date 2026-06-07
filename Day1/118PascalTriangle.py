class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        for i in range(numRows):
            arr = [1]*(i+1) #for every i index row we need i+1 elem/cols
            res.append(arr)
        for i in range(numRows):
            for j in range(1,i):#we need to go upto i and skip the first also so1
                res[i][j] = res[i-1][j] + res[i-1][j-1] #top and top left ka sum
        return res
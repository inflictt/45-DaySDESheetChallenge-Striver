class Solution:
    def median(self, mat):
    	# code here 
    # 	brute idea simple 
    	rows= n = len(mat)
    	cols = len(mat[0])
    	new = []
        for row in mat:
            new.extend(row)
        new.sort()
        medianIdx = (rows*cols)//2
        return new[medianIdx]
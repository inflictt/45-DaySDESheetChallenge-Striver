class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # using binary search appp
        # main concept is. 1d to 2d mapping is 2d row will be now. mid//n and then coll will be mid%n
        n = m = len(matrix)
        n = len(matrix[0])
        lo , hi = 0 , m*n-1 #taking this as 1d array 
        while lo <=hi :
            mid = lo + (hi-lo)//2 #overflow saving 
            if matrix[mid//n][mid%n]>target:#bigger val so bring end down 
                hi = mid-1
            elif matrix[mid//n][mid%n]<target:
                lo = mid +1
            else:#we got the elem
                return True
        return False
                
 

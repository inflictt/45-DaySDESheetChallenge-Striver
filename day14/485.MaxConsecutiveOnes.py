class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0 
        maxi = 0 
        for val in nums:
            if val!=1:
                maxi = max(cnt,maxi)
                cnt=0
            else:#val==1
                cnt+=1
        
        return max(maxi,cnt)
            
                
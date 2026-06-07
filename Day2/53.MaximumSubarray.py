class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxi = 0
        if len(nums)==1:
            return nums[0]
        # case for all -ves
        onePos = False
        for val in nums:
            if val>0:
                onePos = True
                break
            
        if onePos ==False:#means all neg
            return max(nums)
            
        for i in range(len(nums)):
            val = nums[i] #let it be -2 now 
            currSum = val+currSum # 0+-2 = -2
            if currSum<0:
                currSum= 0 
            else:#currSum>0 mtlb ki currSum be 1
                maxi = max(currSum,maxi)
        return maxi
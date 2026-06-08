class Solution:
    def longestSubarray(self, nums, target):  
        
        prefixSumMap = {0:-1}# as by default the prefix sum ofthe  arr would be 0
        res = 0
        cnt = 0
        prefixSum = 0
        # now in the map ill stotre prefixSum:index now 
        for i in range(len(nums)):
            prefixSum += nums[i] #0+10
            diff= prefixSum - target #10-15 = -5 in or not
            if diff in prefixSumMap.keys(): #check if diff in there or not but if ye then
                res = max(res , i  - prefixSumMap[diff])
            # else mtlb ki diff not in there but we have to store the index for that as well
            if prefixSum not in prefixSumMap:
                prefixSumMap[prefixSum] = i
        return res
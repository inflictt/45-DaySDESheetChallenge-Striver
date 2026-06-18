class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i and j ptr 
        # where i always pts the uniq elem and j means find the uniq elm and give to i 
        i = 0 
        j = 1 
        n = len(nums)
        while j < n :
            if nums[i]==nums[j]:#i will need uniq elem so move  up by 1
                j+=1
            else:#j got a uniq elem
                i+=1 #as uske next mai j tha and woh aage chala gya tha means waha pr dupe elm he tha
                nums[i] , nums[j] = nums[j] , nums[i]
                j+=1
        return i+1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # first loop to find the conditionSatisfication index 
        # condition is. aarr[i-1]<arr[i]
        cInd= -1
        for i in range(n-1,0,-1):
            if nums[i-1]<nums[i]:
                cInd = i-1
                break
        # finding the swapping index and then will swap it
        if cInd != -1 :
            swapIndex = cInd
            for i in range(n-1,cInd,-1):
                if nums[cInd]<nums[i]:
                    # swap now 
                    nums[cInd] , nums[i] =nums[i],  nums[cInd]
                    break
        else:
            nums.reverse()
            return nums
        # now i just have to rev the arr from cInd to end and return
        l = cInd+1
        r = n-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
    # steps find the c index and uske baad ki complete rem arr will be in descending order so we just have
    # find the next greater element than c index and swap it and then reverse the rem arr to get the next permutation in place.

    # and if c index remains -1 that means the arr is in descending order and we just have to reverse it to get the next permutation which will be the lowest order.
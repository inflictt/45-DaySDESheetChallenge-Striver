class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # so the target = 0 and target = n1+n2+n2 
        # therefor  0 = n1+n2+n3
        # n2+n3 = -n1 this will be used now
        
        nums.sort()
        final = []
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:continue
            target = -nums[i]#-4 in start 

            lo , hi = i+1 , len(nums)-1
            while lo<hi:
                total = nums[lo]+nums[hi]
                if total<target:
                    lo+=1
                elif total>target:
                    hi-=1
                else:#ttl is now equal to target
                    final.append([nums[i],nums[lo],nums[hi]])
                    lo+=1
                    hi-=1
                    # check if they are dupe or not to prv vals
                    while lo<hi and nums[lo]==nums[lo-1]:
                        lo+=1
                    while hi>lo and nums[hi]==nums[hi+1]:
                        hi-=1
        return final

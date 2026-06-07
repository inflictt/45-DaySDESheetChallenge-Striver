class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 4 big cases  
        # loop 1 for i going upto n-3 as last 3 for loop 2 j  , lo and hi ptr
        # [0,0,0,0,0]
        #    i,j,lo,hi this is how 4 ptr are being used up in here
        # sort first
        nums.sort()#[-2,-1,0,0,1,2]
        #[-2,-1,0,0,1,2]
        # i,j, lo, , ,hi
        # tota, = -2+-1=0+2 =-1  not answer bring low up as not correct
        n = len(nums)
        ans =[]
        for i in range(n-3):   #i->a
            if i>0 and nums[i]==nums[i-1]:continue
            for j in range(i+1,n-2):#j->b
                if j>i+1 and nums[j]==nums[j-1]:continue
                lo = j+1    #lo->c
                hi = n-1    #hi->d
                while lo<hi:
                    total = nums[lo]+nums[hi]+nums[i]+nums[j]
                    if total<target:
                        lo+=1
                    elif total>target:
                        hi-=1
                    else:#got equal
                        ans.append( [ nums[i],nums[j],nums[lo],nums[hi] ] )
                        lo+=1
                        hi-=1
                        while lo<hi and nums[lo]==nums[lo-1]:#we need to check values from which we came here 
                            lo+=1
                        while lo<hi and nums[hi]==nums[hi+1]:#we need to check values from which we came here 
                            hi-=1
                        # Hum check kar rahe hain ki current value kahin us value ke equal toh nahi jo abhi-abhi answer mein use hui thi. Agar equal hai, toh same triplet dubara ban sakta hai, isliye skip kar dete hain.
        return ans
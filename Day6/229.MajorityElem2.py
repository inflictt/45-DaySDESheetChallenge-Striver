class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        c1,v1 = 0 ,None
        c2,v2 = 0 ,None
        for i in range(n):
            if nums[i] == v1:#first checke it matches the 0th elem or not
                c1+=1
            elif nums[i] == v2:#second checke it matches the 1th elem or not
                c2+=1
            elif c1 == 0:#second checke it matches the 1th elem or not
                v1 = nums[i]
                c1= 1
            elif c2==0:#second checke it matches the 1th elem or not
                v2 = nums[i]
                c2 = 1
            else:#bring down both as new diff elem came
                c1-=1
                c2-=1
        c1 , c2 = 0 ,0 
        for num in nums:
            if num == v1:
                c1+=1
            if num ==v2:
                c2+=1
        reqCnt = math.floor(n / 3)
        if c1>reqCnt:
            ans.append(v1)
        if c2>reqCnt:
            ans.append(v2)
        return ans

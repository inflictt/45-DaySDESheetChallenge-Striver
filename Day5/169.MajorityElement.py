class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count ,val1 = 1,nums[0]#took first elm of arr andset countas 1
        for i in range(1,len(nums)):
            # if same count+=1
            # if diff count-=1 
            # if coutn got 0 then udapte the numeber
            if val1 == nums[i]:
                count+=1
            elif val1 != nums[i]:
                count-=1
            if count==0:
                val1=nums[i]
                count = 1
        return val1
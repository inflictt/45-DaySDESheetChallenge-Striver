class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # better approahc as tc and sc both O(n)
        hashMap = {}
        diff = -1
        ans = [-1,-1]
        for i in range(len(nums)):
            num = nums[i]
            diff = target-num#9-2 = 7. check if 7 in map or not
            if diff in hashMap.keys():#false as at i = 0, 7 is not in hm but at i=1 2 is in the hasmap and we need the index of it 
                ans[0] = hashMap[diff]
                ans[1] = i
                return ans
            else:
                hashMap[num] = hashMap.get(num,i)#as index store krwaana hai 
        return ans
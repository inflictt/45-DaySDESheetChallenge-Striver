class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mySet = set()
        for val in nums:
            if val not in mySet:
                mySet.add(val)
            else:
                return val
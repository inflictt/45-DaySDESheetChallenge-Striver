class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # best O(n)
        # we will try to find the first/start of a sequence
        n = len(nums)
        if n == 0 :
            return 0
        # edge cases handled
        mySet = set(nums)

        maxi = 0
        for val in mySet:
            cnt=1
            if val-1 in mySet:#not a start 
                continue
            # now we will got only a start
            if val-1 not in mySet:
                start = val
                while start+1 in mySet:
                    start+=1
                    cnt+=1
            maxi = max(cnt,maxi)
        return maxi
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def solve(i , tmp , output):
            if len(nums) <= i :
                # store the value and return
                output.append(tmp[:])
                return 
            # pick
            tmp.append(nums[i])
            pick = solve(i +1 , tmp , output)
            tmp.pop()
            j = i + 1
            while j< len(nums) and nums[j]==nums[i]:
                j+=1
            notPick = solve(j , tmp , output)

        i =0 
        tmp = []
        output = []
        ans = solve(i , tmp , output)
        return output
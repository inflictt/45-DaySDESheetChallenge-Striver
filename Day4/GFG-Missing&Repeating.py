# link - https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1
class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        # finding dupe first
        s = set()
        ans = [-1,-1]
        for val in arr:
            if val not in s:
                s.add(val)
            else:#already in so mark ans and break
                ans[0] = val
                
        
        # so all ranges start from 1
        mini = 1  
        maxi = n+1#means len is the max num we can go upto +1 as one num is rep also
        new = list(range(mini , maxi))
        for val in new:
            if val not in s:
                ans[1] = val
                break
        return ans

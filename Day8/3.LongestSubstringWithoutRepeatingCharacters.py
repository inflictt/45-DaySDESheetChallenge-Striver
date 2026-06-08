class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Maintain a window [left, right]
        # containing unique characters only.
        # Expand right pointer.
        # If duplicate appears,
        # shrink the window from the left
        # until the duplicate is removed.
        # After every valid window,
        # update maximum length.
        l,r =0 , 0 
        n = len(s)
        maxi , count = 0 , 0
        myDict = dict()
        while r<n: 
            if s[r] in myDict:
                l = max(l, myDict[s[r]] + 1)
                myDict[s[r]] = r
                maxi = max(maxi, r - l + 1)
                # r += 1
            else:# s[r] not in myDict:#my dict nowhai stored value of p : 0 and w:1
                myDict[s[r]] = r
                count =(r - l + 1)
                # r+=1
            r+=1
            maxi = max(maxi,count)
        return maxi
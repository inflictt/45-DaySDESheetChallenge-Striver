class Solution:

    def sumOfLengths(self, arr: list[int]) -> int:
        """code"""
        n = len(arr)
        ans = 0
        for i in range(n):#main one for the outer checking loop going
        # till len of arr/ last elem tell the length only
            seen = set()
            for j in range(i, n):#example the 1 in the 123, 1 would go till 1 to 
                if arr[j] in seen:
                    break
                seen.add(arr[j])
                ans += (j - i + 1)
        return ans
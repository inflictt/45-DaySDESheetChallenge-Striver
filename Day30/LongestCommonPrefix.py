class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        first = strs[0] #flower everytime i will stargt from flower 0th index
        longestCommon = first #by default as flower
        for j in range(1,n):
            i  = 0 
            word = strs[j]
            current = ""
            for ch in word: #flow
                if i<len(first) and ch ==first[i]:#f==f 
                    current = current+ch
                    i+=1
                else: 
                    break
            if len(current)==0:
                return "" #as no common prefix for the current loop we had
            if len(current) < len(longestCommon):
                longestCommon = current
        return longestCommon

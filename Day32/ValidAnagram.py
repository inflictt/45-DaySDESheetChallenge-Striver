from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #  as if i sort the both the words and check if both are equal than it an anagram else not , 
        # sortedS = sorted(s)
        # sortedT = sorted(t)
        # return sortedS==sortedT
        # also if i geth the each element frequqncy and then check if all matched then it working 
        return Counter(s)==Counter(t)

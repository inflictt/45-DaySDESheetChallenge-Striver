class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse=True)
        g.sort(reverse=True)
        cnt = 0 
        i , j = 0 , 0
        # greedya approahc as sorted indescing and will give now the largest size candie to largest greedy child
        while i < len(g) and j < len(s):
            if s[j]>=g[i]:#means we can assign the cookie now 
                cnt+=1
                i+=1
                j+=1
            else:
                i+=1 #as the cookie remains with me not the greed of the child
                continue
            
        return cnt
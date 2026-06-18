class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return ''.join(list(map(str, (list(permutations(list(range(1, n+1))))[k-1]))))

        
        
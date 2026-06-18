class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve(index, inp ,temp, final):
            if len(inp)==index:
                # store and return
                final.append(temp[:])
                return 
            # pick then explore other vairations 
            for i in range(len(inp)):
                val = inp[i]
                if val not in temp:
                    temp.append(val)
                    solve(index+1, inp ,temp, final)
                    # pop and then we will backtrack
                    temp.pop()
        final = []
        solve(0, nums ,[] , final)
        return final
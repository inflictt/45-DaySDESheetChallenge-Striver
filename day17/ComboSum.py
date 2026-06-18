class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(idx ,tSum ,temp , output):
            if tSum == 0 :
                # store values
                # nd return 
                output.append(temp[:])
                return 
            if tSum < 0:
                # return back
                return
            if idx>=len(candidates):
                if tSum==0:#store it
                    output.append(temp[:])
                return 
            # we have to pick each step until it hits any of the base case 
            # pick
            temp.append(candidates[idx])
            solve(idx ,tSum - candidates[idx] , temp , output)
            # explore all possiblities 
            temp.pop()
            solve(idx +1 , tSum  ,temp , output)
        output = []
        solve(0 , target  ,[] , output)
        return output
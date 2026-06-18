class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def solve(i , target , temp , output):
            if target == 0 :
                output.append(temp[:])
                return 
            if target<0:
                return
            if i>=len(candidates):
                if target == 0 :
                    output.append(temp[:])
                return 
            # base cases handled now just pick and not pick and no reps allowed
            temp.append(candidates[i])
            pick = solve(i +1, target - candidates[i] , temp , output)
            temp.pop()
            j = i+1
            while j<len(candidates) and candidates[j] == candidates[i]:
                j+=1
            notPick = solve(j , target , temp , output)

        output = []
        solve(0 , target , [] , output)
        return output
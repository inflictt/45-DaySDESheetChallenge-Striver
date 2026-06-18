class Solution:
    def fractionalKnapsack(self, val, wt, W):
        #code here
        # Input: val[] = [60, 100, 120], wt[] = [10, 20, 30], capacity = 50
        n= len(val)
        ratios = [(val[i],wt[i],(val[i]/wt[i])) for i in range(n)]
        ratios = sorted(ratios,key=lambda x : x[2],reverse = True)
        # [
        #     (60, 10, 6.0),
        #     (100, 20, 5.0),
        #     (120, 30, 4.0)
        # ]
        total = 0
        for i in range(n):
            currW = ratios[i][1]
            ratio = ratios[i][2]
            currVal = ratios[i][0]
            if W>=currW:
                total += currVal
                W -=currW
            else:#W<currW
                total += (W*ratio)
                break
        return total
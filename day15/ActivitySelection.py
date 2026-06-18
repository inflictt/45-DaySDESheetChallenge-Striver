class Solution:
    def activitySelection(self, start, finish):
        #code  
        
        activities = []

        for i in range(len(start)):
            activities.append((start[i], finish[i]))
        
        activities.sort(key=lambda x: x[1])
        
        n = len(activities)
        # soritng off by finish time 
        prevEnd = -1
        ans = []
        for i in range(n):
            currStart = activities[i][0]
            currEnd = activities[i][1]
            if prevEnd<currStart and currStart<=currEnd:
                ans.append((currStart,currEnd))
                prevEnd = currEnd
                
        return len(ans)
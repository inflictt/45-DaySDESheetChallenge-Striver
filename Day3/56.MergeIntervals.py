
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new1 = sorted(intervals,key = lambda x : x[0])
        ans = []
        n = len(new1)
        i = 1
        # assuming rhe first is the first interval ->=[1,3]
        curr = new1[0]
        currStart ,currEnd = curr[0],curr[1]
        while i<n:#i denotes the interavl we are on
            # here i is 1 = 2,6 is we are on
            # check if we in the prev interval and extend or make a new one
            new = new1[i]#which is 2,6
            newStart ,newEnd = new[0],new[1]#2,6
            if currEnd>=newStart:#3>=2 
                # so extend current interval
                currEnd = max(currEnd,newEnd)
        # now  currstart ,currend = 1,6
            else:# currEnd>newStart:#6>8 false so new currstartnd end req
                intvl = [currStart,currEnd]
                ans.append(intvl)
                currStart ,currEnd = newStart,newEnd
            i+=1
        ans.append([currStart,currEnd])#last interaval always get aded now

        return ans


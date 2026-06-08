class Solution:
    def subarrayXor(self, nums, target):
        # code here
        # idea is that have a map storingthe values the xor that came 
        # map - > default at 
        xorPrefixMap = {0: 1}
        count,currXorPrefix= 0 , 0
        
        for i in range(len(nums)):
            currXorPrefix ^= nums[i] # 5 xor 6 is 3 check 3 in map or not
            diffXor = currXorPrefix ^ target#check 3 in map or not
            # +x is undone by -x
            # ^x is undone by ^x
            if diffXor in xorPrefixMap.keys():
                # if yes then store them
                count += xorPrefixMap[diffXor]#pehele kitni time show up kia so storing that
            # now else ab nhi toh we need to store ther currprefix of sum
            xorPrefixMap[currXorPrefix]  = xorPrefixMap.get(currXorPrefix,0)+1
            # ye agar store ni hoga to 0 se bhej dega aur + 1 increment krdega 
        return count 
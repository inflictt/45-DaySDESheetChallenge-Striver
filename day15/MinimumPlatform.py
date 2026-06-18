class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        
        arr.sort()
        dep.sort()
        maxPlat = 1
        ans= 0 
        prevDep = -1
        n = len(arr)
        i , j = 0 , 0 
        while i <n and j<n:
            if dep[j]<arr[i]:#means the prev train can leave now
                maxPlat -=1
                j+=1
            elif arr[i]<=dep[j]:#koi train already hai plat par aur ek new train aagyi toh platform badahan hai
                maxPlat+=1
                i+=1
            ans = max(ans,maxPlat)
        return ans-1
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeCombine(left,right,cnt):
            i , j = 0 , 0 
            m , n = len(left) , len(right)
            ans=[]
            while i<m and j<n:
                if left[i]>(2*right[j]):
                    cnt += m-i
                    j+=1
                else:
                    i+=1

            i , j = 0 , 0 
            while i<m and j<n:
                if left[i]<right[j]:
                    
                    ans.append(left[i])
                    i+=1
                else:
                    
                    ans.append(right[j])
                    j+=1
            if i < m :
                while i < m :#if something is still in inthere 
                    ans.append(left[i])
                    i+=1
            if j<n:
                while j<n:
                    ans.append(right[j])
                    j+=1
            return ans ,cnt

        def mergeSort(nums , cnt ):
            n =  len(nums)
            if n<=1:
                return nums , 0 
            mid = n//2
            leftArr = nums[:mid]
            rightArr = nums[mid:]
            left,lc =  mergeSort(leftArr , cnt)
            right,rc =  mergeSort(rightArr, cnt)
            merged , mc = mergeCombine(left,right , cnt)
            return  merged , mc+lc+rc
        cnt = 0 
        _ , ans = mergeSort(nums , cnt )
        return ans
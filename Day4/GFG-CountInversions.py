# ques - https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
class Solution:
    def inversionCount(self, nums):
        # Code Here
        def mergeCombine(left,right,count):
            ans = []
            i , j = 0 ,0 
            m , n = len(left) , len(right)
            while i < m and j < n :
                # main logic
        #  Inversion count is the number of pairs of elements (i, j)
        # such that i < j and arr[i] > arr[j].
                if left[i] > right[j]:
                    count += m-i 
                    ans.append(right[j])
                    j+=1
                else:
                    ans.append(left[i])
                    i+=1
            if i<m:
                while i<m:
                    ans.append(left[i])
                    i+=1
            if j<n:
                while j<n:
                    ans.append(right[j])
                    j+=1
            return ans , count
        def mergeSort(nums,count):
            n = len(nums)
            if n<=1:
                return nums , 0
            mid = n//2
            left,lc =mergeSort(nums[:mid],count)
            right,rc =mergeSort(nums[mid:],count)
            finalarr , fc = mergeCombine(left,right,count)
            return finalarr , fc+lc+rc 
        count = 0 
        arr , ans = mergeSort(nums,count)
        return count #or as well ans willhave the samew 
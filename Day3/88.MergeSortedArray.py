class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged = []
        i, j = 0 , 0 
        while i<m and j <n:
            if nums1[i]<nums2[j]:
                merged.append(nums1[i])
                i+=1
            else:
                merged.append(nums2[j])
                j+=1
        if i<m :
            while i<m:
                merged.append(nums1[i])
                i+=1
        if j<n :
            while j<n:
                merged.append(nums2[j])
                j+=1
        nums1[:] = merged
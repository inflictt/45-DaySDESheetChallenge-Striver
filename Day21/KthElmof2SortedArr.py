class Solution:
    def kthElement(self, a, b, k):
        # code here
        # brute - join sort and return kth elem 
        def mergeCombine( nums1, nums2):
            i = j = 0
            arr = []
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    arr.append(nums1[i])
                    i += 1
                else:
                    arr.append(nums2[j])
                    j += 1
            while i < len(nums1):
                arr.append(nums1[i])
                i += 1
            while j < len(nums2):
                arr.append(nums2[j])
                j += 1
            return arr
        mergedArr = mergeCombine( a, b)
        # so now i have the merge sorted array i ned to only return the k - 1 index thats ti
        return mergedArr[k-1]
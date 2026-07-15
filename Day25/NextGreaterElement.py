class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1 for _ in range(len(nums2))]
        stack = []
        # loop over nums2 as ill create for the complete nums2 arr
        for i in range(len(nums2) - 1, -1, -1):
            if (
                len(stack) == 0
            ):  # means e,mpty so store -1 means conitnue and add current val
                stack.append(nums2[i])
                continue
            else:  # stack not null hold some value in it
                upcomVal = nums2[i]
                while len(stack) != 0 and stack[-1] < upcomVal:
                    stack.pop()
                    # if empty hogya stack return -1 else jo value top par h woh ans
                if len(stack) != 0:
                    ans[i] = stack[-1]
                    stack.append(nums2[i])
                else:
                    stack.append(nums2[i])
        mp = {}
        for i in range(len(nums2)):
            mp[nums2[i]] = ans[i]

        final = []
        for i in range(len(nums1)):
            num1 = nums1[i]
            toAdd = mp[num1]
            final.append(toAdd)
        return final

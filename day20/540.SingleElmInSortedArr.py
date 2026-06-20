class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        def isOdd(idx):
            return idx % 2 == 1
            
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            # Pair is (mid-1, mid)
            if mid > 0 and nums[mid] == nums[mid - 1]:
                # mid is second index of the pair
                if isOdd(mid):
                    # normal pairing, single lies right
                    lo = mid + 1
                else:
                    # pairing shifted, single lies left
                    hi = mid - 2

            # Pair is (mid, mid+1)
            elif mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                # mid is first index of the pair
                if isOdd(mid):
                    # shifted pairing, single lies left
                    hi = mid - 1
                else:
                    # normal pairing, single lies right
                    lo = mid + 2
            # No pair found
            else:
                return nums[mid]
        return nums[lo]
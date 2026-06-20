class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low , high = 0 , len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            # elif in right sorted sode
            if nums[mid]<=nums[high]:#for evem 1,34,59,123,324 mid is at 59 and high at 324
                # check if thaat sorted part has elem or not 
                if nums[mid]<=target<=nums[high]:#if here then low= mid+1
                    low= mid+1
                else:#nhi hai us right sorted part mai toh high niche le aao
                    high = mid-1
            else:#ki left wala sorted hai
                if nums[low]<=target<=nums[mid]:#if here then low= mid+1
                    high = mid - 1 
                else:
                    low = mid + 1 
        return -1
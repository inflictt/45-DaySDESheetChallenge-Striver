class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0,0,0]

        for val in nums:
            arr[val] += 1
        idx = 0

        for color in range(3):
            
            for _ in range(arr[color]):
                nums[idx] = color
                idx += 1
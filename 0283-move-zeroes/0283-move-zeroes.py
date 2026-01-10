class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stablePointer = 0
        movingPointer = 1

        while movingPointer < len(nums):
            if nums[movingPointer] != 0 and nums[stablePointer] ==0:
                nums[stablePointer],nums[movingPointer] = nums[movingPointer],nums[stablePointer]
                stablePointer = stablePointer +1
            if nums[stablePointer] !=0:
                stablePointer = stablePointer+1
            movingPointer = movingPointer +1

        # if movingPointer == len(nums)-1:
        #     while stablePointer <= len(nums)-1:
        #         nums[stablePointer] =0
        return nums

        
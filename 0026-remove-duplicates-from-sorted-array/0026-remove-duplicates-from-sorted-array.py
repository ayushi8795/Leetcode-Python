class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [ ]
        right = 1
        left = 1
        while right <len(nums):
            if nums[right] == nums[right-1]:
                right = right +1
            else:
                nums[left] = nums[right]
                left = left+1
                right = right +1

        return left 
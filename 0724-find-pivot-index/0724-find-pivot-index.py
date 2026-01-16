class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum =0
        for index, value in enumerate(nums):
            # right = totalSum-leftSum-value hence did not use right, replace directly
            if leftSum == totalSum-leftSum-value:
                return index
            leftSum = leftSum + value
        return -1
        
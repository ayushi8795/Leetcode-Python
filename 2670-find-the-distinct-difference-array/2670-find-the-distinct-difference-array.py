class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        diff = [0]*len(nums)

        for i in range(len(nums)):
            diff[i] = len(set(nums[:i+1]))-len(set(nums[i+1:]))
        return diff
        
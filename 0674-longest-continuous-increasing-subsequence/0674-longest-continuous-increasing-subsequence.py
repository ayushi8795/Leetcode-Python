class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = max_len = 1

        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                count+=1
            else:
                count = 1
            max_len = max(max_len,count)
        return max_len
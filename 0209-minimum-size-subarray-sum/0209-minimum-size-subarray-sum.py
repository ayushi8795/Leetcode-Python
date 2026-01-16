class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = sum(nums)

        if total < target:
            return 0
        
        if target in nums:
            return 1

        minx = len(nums)
        lsum = 0
        left = 0

        for right in range(len(nums)):
            lsum = lsum +nums[right]
            while lsum >= target:
                minx = min(minx,right-left+1)
                lsum = lsum -nums[left]
                left = left +1

        return minx
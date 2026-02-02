class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        
        # cost of first subarray is fixed
        first_cost = nums[0]
        
        # minimum value seen so far for second subarray start
        min_second = float('inf')
        answer = float('inf')
        
        # i starts from 1 because second subarray must start after index 0
        # j must be at least i+1 so third subarray is non-empty
        for i in range(1, n - 1):
            min_second = min(min_second, nums[i])
            answer = min(answer, min_second + nums[i + 1])
        
        return first_cost + answer
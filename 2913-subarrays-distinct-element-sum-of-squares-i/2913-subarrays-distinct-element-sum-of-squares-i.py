class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        
        for i in range(len(nums)):
            for j in range(i, len(nums)+1):
                total = total + len(set(nums[i:j]))**2
        return total

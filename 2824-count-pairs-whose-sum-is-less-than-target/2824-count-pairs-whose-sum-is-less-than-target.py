class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        end = len(nums)
        count = 0

        for i in range(len(nums)):
            start = i 
            nextP = i+1
            
            while start < nextP <end:
                if nums[start] + nums[nextP] < target:
                    count = count+1
                nextP = nextP+1
        return count
        
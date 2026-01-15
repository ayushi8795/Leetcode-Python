class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        b = 0
        for i in nums:
            b = b + i
            result.append(b)
        return result
    

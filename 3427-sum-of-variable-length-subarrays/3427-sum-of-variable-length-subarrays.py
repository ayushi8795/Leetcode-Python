class Solution:
    def subarraySum(self, nums: List[int]) -> int:

        n = len(nums)
        res = 0

        if n == 1:
            return nums[0]

        for i in range(n):
            start = max(0,i-nums[i])
            summ = 0
            for j in range(start, i+1):
                summ = summ + nums[j]
            res = res+summ
        return res

        
        

        
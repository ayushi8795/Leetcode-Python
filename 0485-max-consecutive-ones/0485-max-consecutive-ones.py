class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = -1
        count = 0

        for i in nums:
            if i == 1:
                count = count+1
            else:
                count = 0
            maxi = max(maxi,count)
        return maxi
        
        
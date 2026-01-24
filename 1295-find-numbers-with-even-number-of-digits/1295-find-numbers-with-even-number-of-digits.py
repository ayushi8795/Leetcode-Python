class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evenCount = 0

        for i in nums:
            if len(str(i))%2 ==0:
                evenCount +=1
        return evenCount
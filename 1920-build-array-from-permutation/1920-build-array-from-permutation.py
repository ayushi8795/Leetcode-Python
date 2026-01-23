class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        newNums = []
        for i in range(len(nums)):
            newNums.insert(i,nums[nums[i]])
        return newNums
        
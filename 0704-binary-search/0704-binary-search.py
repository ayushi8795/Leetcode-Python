class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lowerBound = 0 #index
        upperBound = len(nums)-1 #index
        while lowerBound <= upperBound:
            middle = (upperBound + lowerBound)//2

            if target < nums[middle]:
                upperBound = middle -1
            elif target > nums[middle]:
                lowerBound = middle +1
            elif target == nums[middle]:
                return middle
        return -1
        
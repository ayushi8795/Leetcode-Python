class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0

        for i in range(len(nums)):

            right = totalSum-leftSum-nums[i]

            if leftSum == right:
                return i
            #  The reason left sum id added after if statement is because ques never mentions 
            # to add the middleindex before checking the equality of left and right sum
            leftSum = leftSum + nums[i]
        return -1
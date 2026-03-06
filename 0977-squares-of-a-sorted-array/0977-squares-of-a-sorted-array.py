class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)

        left = 0 
        right = len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -=1
            else:
                square = nums[left]
                left+=1
            res[i] = square**2
        return res
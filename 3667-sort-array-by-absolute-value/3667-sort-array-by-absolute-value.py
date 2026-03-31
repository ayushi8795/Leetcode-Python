class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
    


        for i in range(len(nums)):
            start = i+1
            while start < len(nums):
                if abs(nums[start]) < abs(nums[i]):
                    nums[start],nums[i] = nums[i],nums[start]
                start = start +1
        return nums

            

        


        
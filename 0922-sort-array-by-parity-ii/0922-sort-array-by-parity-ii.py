class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evenindex = 0
        oddindex = 1

        while evenindex < len(nums) and oddindex < len(nums):
            if nums[evenindex]%2 ==0:
                evenindex = evenindex+2
            if nums[oddindex]%2 ==1:
                oddindex = oddindex + 2
            else:
                nums[evenindex],nums[oddindex] = nums[oddindex] ,nums[evenindex]
        return nums
        
    
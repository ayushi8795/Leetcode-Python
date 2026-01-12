class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        rightP= len(nums)-1
        leftP=0

        while 0<=leftP<rightP<len(nums):
            if nums[leftP]%2 != 0 and nums[rightP]%2 ==0:
                nums[leftP],nums[rightP] = nums[rightP],nums[leftP]
                leftP = leftP +1
                rightP =rightP-1
            elif nums[leftP]%2 == 0:
                leftP+=1
            elif nums[rightP]%2 !=0:
                rightP-=1
        return nums

        
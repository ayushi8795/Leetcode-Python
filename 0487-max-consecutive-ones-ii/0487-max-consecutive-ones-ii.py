class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        seq = 0
        left , right = 0,0
        nums_zero = 0

        while right < len(nums):
            if nums[right] == 0:
                nums_zero +=1
            
            while nums_zero == 2:
                if nums[left] == 0:
                    nums_zero -=1
                left = left+1
            seq = max(seq, right-left+1)
            right+=1
        return seq
            

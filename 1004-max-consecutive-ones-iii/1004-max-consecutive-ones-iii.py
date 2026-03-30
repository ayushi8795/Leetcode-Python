class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left = 0
        count = 0 
        curr = 0 

        for right in range(len(nums)):
            if nums[right] ==0:
                curr+=1

            while curr > k:
                if nums[left] == 0: #reduce curr with every left shift so that fresh k can be start.
                    curr = curr-1
                left+=1
            count = max(count, right-left+1)

        return count
        

            


        
class Solution:
    def countPartitions(self, nums: List[int]) -> int:

        summ = 0
        count = 0
        leftSum = 0
        for i in range(len(nums)):
            summ = summ + nums[i]

        for i in range(len(nums)-1):
            leftSum = leftSum +nums[i]
            rightSum = summ-leftSum
            if (leftSum-rightSum)%2 == 0:
                count = count+1
        return count


            

        
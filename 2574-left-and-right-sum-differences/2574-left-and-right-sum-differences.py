class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums) ==1:
            return [0]

        leftSum = []
        rightSum =[]
        res = []
        summ = 0

        for i in range(len(nums)):
            if i == 0:
                leftSum.append(0)
            else:
                leftSum.append(leftSum[i-1]+nums[i-1])
            summ = summ + nums[i]
        

        # Right would be adding everthing in right of index. If we have summ we can minus the value at each index from total sum to get rightSum
        for i in range(len(nums)):
            summ = summ-nums[i]
            rightSum.append(summ)

        for i in range(len(leftSum)):
            res.append(abs(leftSum[i] - rightSum[i]))
        return res
        

            

            
            

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        rangeList = []
        numsLen = len(nums)
        # if nothing in list
        if numsLen== 0:
            rangeList.append([lower,upper])
            return rangeList

        #  if no  0 in list
        if lower < nums[0]:
            rangeList.append([lower,nums[0]-1])
        
        for i in range(numsLen-1):
            if nums[i+1] - nums[i] <= 1:
                continue
            rangeList.append([nums[i]+1, nums[i+1]-1])
        
        # if no 99 in list
        if upper > nums[numsLen-1]:
            rangeList.append([nums[numsLen-1]+1,upper])
        
        return rangeList
        

                
                

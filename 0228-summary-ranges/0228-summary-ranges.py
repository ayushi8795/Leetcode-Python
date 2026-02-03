class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        rangex = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i+1 < len(nums) and nums[i+1] - nums[i] == 1:
                i = i+1

            if start != nums[i]:
                rangex.append(str(start) + "->" + str(nums[i]))
            else:
                rangex.append(str(nums[i]))
            
            i =i +1

        return rangex



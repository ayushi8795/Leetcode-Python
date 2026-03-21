class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        start_index = 0 
        end_index = len(nums)-1
        concatValue = 0

        while start_index <= end_index:
            if start_index != end_index:
                concatValue =concatValue +  int(str(nums[start_index]) + str(nums[end_index]))
            else:
                concatValue =concatValue + nums[start_index]
            start_index+=1
            end_index = end_index-1
        return concatValue

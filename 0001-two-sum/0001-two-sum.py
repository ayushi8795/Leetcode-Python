class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dicc ={}
        
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in dicc:
                return [i,dicc[num2]]
            dicc[nums[i]] = i
        return []


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        result = []
        dic = {}
        for j in range(len(nums)):
            if nums[j] not in dic:
                dic[nums[j]] = 1
            else:
                dic[nums[j]] +=1
                result.append(nums[j])
                break

        for i in range(1,len(nums)+1):
            if i not in nums:
                result.append(i)
        return result

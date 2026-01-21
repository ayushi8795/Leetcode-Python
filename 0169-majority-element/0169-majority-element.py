class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        n = len(nums)
        for i in nums:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i]+=1
            
            if dic[i] > int(n/2):
                    return i

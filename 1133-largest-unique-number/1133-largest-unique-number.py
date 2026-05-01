class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        res = -1

        hashi = {}

        for i in nums:
            if i not in hashi:
                hashi[i] = 1
            else:
                hashi[i] = hashi[i]+1
        
        for key,value in hashi.items():
            if value == 1:
                res = max(res,key)
        return res
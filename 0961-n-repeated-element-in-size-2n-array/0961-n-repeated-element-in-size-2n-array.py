class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2

        hashi = {}

        for i in nums:
            if i not in hashi:
                hashi[i] = 1
            else:
                hashi[i] = hashi[i]+1

        for key,value in hashi.items():
            if value == n:
                return key
        
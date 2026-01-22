class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        fre = {}

        for i in nums:
            if i not in fre:
                fre[i] = 1
            else:
                return True
        return False
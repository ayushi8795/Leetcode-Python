class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len( nums)
        fre = {}
        lis =[]
        for i in nums:
            if i not in fre:
                fre[i] = i
        for i in range(1, length+1):
            if i not in fre:
                lis.append(i)
        return lis

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        lis = []

        for nu in nums:
            if nu not in dic:
                dic[nu] =1
            else:
                dic[nu] = dic[nu]+1
        for key, value in dic.items():
            if value > 1:
                lis.append(key)
        return lis
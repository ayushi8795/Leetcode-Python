class Solution:
    def maxDistinct(self, s: str) -> int:
        dic = {}

        for i in s:
            if i not in dic:
                dic[i] = True
        return len(dic)
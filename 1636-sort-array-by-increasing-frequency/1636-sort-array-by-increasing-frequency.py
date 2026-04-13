class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hashi = {}

        for i in nums:
            if i not in hashi:
                hashi[i] = 1
            else:
                 hashi[i] =  hashi[i] + 1
        hash_ord = sorted(hashi.items(), key=lambda item: (item[1], -item[0]))
        lis = []
        for key,value in hash_ord:
            lis.extend([key]*value)
        return lis
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashi = {}

        for i in arr:
            if i not in hashi:
                hashi[i] = 1
            else:
                hashi[i] =hashi[i]+1
        return len(set(hashi.values())) == len(hashi)
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:

        dictCal = {}

        for index,s in enumerate(s):
            dictCal[s] = index

        for index,t in enumerate(t):
            if t in dictCal:
                dictCal[t] = abs(dictCal[t] - index)
        
        return sum(dictCal.values())
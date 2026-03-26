class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        
        hashi = {}
        res = []

        for arr in arrays:
            for num in arr:
                if num not in hashi:
                    hashi[num] =1
                else:
                    hashi[num]+=1
                
                if hashi[num] == len(arrays):
                    res.append(num)
        return res
            
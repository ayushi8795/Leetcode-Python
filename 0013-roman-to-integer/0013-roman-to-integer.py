class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        output = 0
        right = len(s)-1

        while right>=0:
            if right-1 >= 0 and ((s[right] in ["V","X"] and s[right-1] =="I") or (s[right] in ["L","C"] and s[right-1] =="X") or(s[right] in ["D","M"] and s[right-1] =="C")):
                output = output + dic[s[right]]-dic[s[right-1]]
                right = right - 2
            else:
                output = output + dic[s[right]]
                right = right -1
        return output
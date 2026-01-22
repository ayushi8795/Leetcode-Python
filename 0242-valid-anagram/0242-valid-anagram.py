class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        dicS = {}
        dicT = {}

        n = len(s)  # since len is same for both string  we can create 2 dic using any one's length 

        for i in range(n):
            if s[i] not in dicS:
                dicS[s[i]] = 1
            else:
                dicS[s[i]] = dicS[s[i]]+1

            if t[i] not in dicT:
                dicT[t[i]] = 1
            else:
                dicT[t[i]] = dicT[t[i]]+1

        for key,value in dicS.items():
            if key not in dicT or dicS[key] != dicT[key]:
                return False
        return True
        

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        newS = ''
        n = k

        for i in range(len(s)-1, -1 ,-1):
            if s[i] != '-':
                newS = s[i].upper() + newS
                n  = n-1
                if n == 0:
                    n = k
                    newS = '-' + newS
            else:
                newS = newS + ""
        if len(newS) > 1:
            if newS[0] == '-':
                newS = newS.replace('-', "", 1)
        
        return newS
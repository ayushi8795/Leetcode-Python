class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0
        left=0

        dic = {'0':0,"1":0}

        for right in range(len(s)):
            dic[s[right]] +=1
            while dic['0'] > k and dic['1'] >k:
                # here left means, what ever the value is at that left pointer
                dic[s[left]]-=1
                left = left+1
            res = res + (right-left+1)
        return res

                
            
        
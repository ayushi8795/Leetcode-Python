class Solution:
    def maxScore(self, s: str) -> int:
        sum1 = 0
        zero =0
        ans = 0
        for i in s:
             if i == '1':
                sum1 = sum1 + 1
                
        #-1 because loop needs to stop at len(s)-2 since right cannot be empty
        for i in range(len(s)-1):
            # this if-else block aims at moving 1 element from right to left, if we move 0 to left we increase zero in left substring and if we move 1 from right to left we decrese 1 in right substring
            if s[i] == "0":
                zero = zero+1
            else:
                sum1 = sum1-1
            ans = max(ans , zero+sum1)
        return ans
        
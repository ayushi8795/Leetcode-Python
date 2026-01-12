class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def Checkpali(s):
            start = 0
            end = len(s)-1

            while start <= end:
                if s[start] == s[end]:
                    start = start +1
                    end = end-1
                else:
                    return False
            return True

        if not s : 
            return 0
        if Checkpali(s):
            return 1
        else:
            return 2
                

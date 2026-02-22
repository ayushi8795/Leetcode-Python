class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        count = 0
        hashi ={}

        for i in range(k):
            if s[i] not in hashi:
                hashi[s[i]] =1
            else:
                hashi[s[i]] = hashi[s[i]]+1
        if len(hashi) == k:
            count = count+1

    
        for c in range(k, len(s)):
            #remove or reduce by 1 the freq 1st char when moving a slider window by 1 forward
            hashi[s[c-k]] = hashi[s[c-k]] -1
            if hashi[s[c-k]] == 0:
                del hashi[s[c-k]]

            if s[c] not in hashi:
                hashi[s[c]] = 1
            else:
                hashi[s[c]] = hashi[s[c]] + 1
            
            if len(hashi) == k:
                count = count+1
        return count
        

        
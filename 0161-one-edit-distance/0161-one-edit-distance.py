class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        ns = len(s)
        nt = len(t)

        if ns > nt:
            return self.isOneEditDistance(t,s)

        #  t is always greater than s hence abs is not required [above if stament reverses as soon as s > t]
        if nt - ns > 1:
            return False
        
        for i in range(ns):
            if s[i] != t[i]:

                if ns == nt:
                    return s[i+1 :] == t[i+1 :]   # if 1st different char found check if substring is equal
                else:
                    return s[i:] ==t[i+1 :] # if t is greater increment by 1 pointer and check substring
        
        return ns+1== nt

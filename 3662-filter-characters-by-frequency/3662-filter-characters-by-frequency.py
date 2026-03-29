class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        hashi = OrderedDict()

        for i in s:
            if i not in hashi:
                hashi[i] = 1
            else:
                hashi[i] = hashi[i]+1
        
        for c,ctr in hashi.items():
            if ctr >= k:
                s = s.replace(c,"")
        return s
    
        
        
        
        
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sdict = self.hashcreate(s)
        tdict = self.hashcreate(t)
        count = 0
        for key,value in sdict.items():

            if key in tdict:
                if tdict[key] < value:
                    count = count + value-tdict[key]
            else:
                count = count + value
        return count

    def hashcreate(self,s):
        hashi = {}
        for i in s:
            if i not in hashi:
                hashi[i] = 1
            else:
                hashi[i] = hashi[i]+1
        return hashi

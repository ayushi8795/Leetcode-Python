class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashi = {}
        
        for word in strs:
            strWord = "".join(sorted(word))
            if strWord not in hashi:
                hashi[strWord] = [word]
            else:
                hashi[strWord].append(word)
        
        return [values for key,values in hashi.items()]
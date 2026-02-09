class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashi = {}
        
        for word in strs:
            key = "".join(sorted(word))
            if key not in hashi:
                hashi[key] = [word]
            else:
                hashi[key].append(word)

        return list(hashi.values())
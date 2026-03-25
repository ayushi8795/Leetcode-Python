class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        lep = len(pref)

        for i in words:
            if i[:lep] == pref:
                count+=1
        return count
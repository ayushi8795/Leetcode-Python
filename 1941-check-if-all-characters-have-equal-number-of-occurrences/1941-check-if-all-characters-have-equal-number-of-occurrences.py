class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hashi = {}

        for char in s:
            if char not in hashi:
                hashi[char] =1
            else:
                hashi[char] = hashi[char]+1
        return len(set(hashi.values())) == 1
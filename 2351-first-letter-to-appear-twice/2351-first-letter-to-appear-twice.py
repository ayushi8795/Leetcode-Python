class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        hashi = defaultdict(set)

        for i in range(len(s)):
            if s[i] not in hashi:
                hashi[s[i]].add(i)
            else:
                return s[i]
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set()
        res = 0

        for string in words:
            if string[::-1] in seen:
                res+=1
            else:
                seen.add(string)
        return res
        
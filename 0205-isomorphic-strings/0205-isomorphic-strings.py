class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def extractIndex(s):
            indexMap = {}
            str1 = []

            for char in s:
                if char not in indexMap:
                    indexMap[char] = s.index(char)
                str1.append(str(indexMap[char]))
            return " ".join(str1)

        return extractIndex(s) == extractIndex(t)
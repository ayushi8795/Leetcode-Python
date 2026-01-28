class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        count = 0
        wordDic = enumerate(wordsDict)
        indexWord1 = indexWord2 = -1

        for index, word in wordDic:
            if word == word1:
                indexWord1 = index
            elif word == word2:
                indexWord2 = index

            if indexWord1 != -1 and indexWord2 != -1:
                if count != 0:
                    count = min(count, abs(indexWord1-indexWord2))
                else:
                    count = abs(indexWord1-indexWord2)
        return count

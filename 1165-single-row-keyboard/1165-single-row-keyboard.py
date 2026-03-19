class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        alphadict = {}
        curr = 0
        total_time = 0

        for index,k in enumerate(keyboard):
            alphadict[k] = index

        
        for w in word:
            total_time = total_time + abs(curr-alphadict[w])
            curr = alphadict[w]
        return total_time
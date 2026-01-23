class Solution:
    def maxDistance(self, words: List[str]) -> int:
        maxi = 0

        for i in range(len(words)):
            initial = words[i]
            for j in range(i, len(words)):
                if words[j] != initial:
                    dis = j-i+1
                    maxi = max(maxi, dis)
        return maxi
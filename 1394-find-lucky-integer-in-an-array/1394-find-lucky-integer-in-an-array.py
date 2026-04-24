class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hset = set()
        hashTab = {}

        for i in arr:
            if i not in hashTab:
                hashTab[i] =1
            else:
                hashTab[i]=hashTab[i]+1

        for key,value in hashTab.items():
            if key == value:
                hset.add(key)

        return max(hset) if hset else -1
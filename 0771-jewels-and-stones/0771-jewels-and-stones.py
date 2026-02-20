class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stonedic = {}
        count = 0

        for char in stones:
            if char not in stonedic:
                stonedic[char] = 1
            else:
                stonedic[char] += 1
        
        for key,value in stonedic.items():
            if key in jewels:
                count = count+ value
        return count
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = -1
        leftPointer = 0
        

        while leftPointer <= len(blocks)-k:
            counter = 0
            for i in range(leftPointer , leftPointer+k):
                if blocks[i] == "W":
                    # blocks[i] = "B"
                    counter = counter + 1
            if ans == -1:
                ans = counter
            else:
                ans = min(ans,counter)
            leftPointer +=1
        return ans

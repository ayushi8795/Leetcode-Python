class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        # sumA -x+y = sumB+x-y
        #2(y-x) = sumB-sumA
        # y = (sumB-sumA)//2 +x
        # diff = (sumB-sumA)//2
        # y = x+ diff

        diff = (sumB-sumA)//2
        bobset = set(bobSizes)

        for x in aliceSizes:
            y = x+diff
            if y in bobset:
                return [x,y]


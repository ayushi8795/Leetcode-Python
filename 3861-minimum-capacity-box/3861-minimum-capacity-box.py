class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        mincap = -1
        indexReturn = -1

        for index,cap in enumerate(capacity):
            if cap >= itemSize:
                if mincap == -1:
                    mincap = cap
                    indexReturn = index
                elif mincap > cap :
                    mincap = cap
                    indexReturn = index
        return indexReturn

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        if reader.get(0) == target:
            return 0
        
        lower = 0
        higher = 1

        # gets the boundry of the array
        while reader.get(higher) < target:
            lower = higher
            higher = higher*2

        
        while lower <= higher:
            mid = (lower+higher)//2
            num = reader.get(mid)

            if num == target:
                return mid
            elif num < target:
                lower = mid+1
            else:
                higher = mid-1
        return -1
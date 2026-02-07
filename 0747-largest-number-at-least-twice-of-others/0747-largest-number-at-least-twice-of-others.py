class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        largest = second_largest = -1
        index = -1


        for i,n in enumerate(nums):

            if n >= largest:
                second_largest, largest = largest, n
                index = i
            elif n >= second_largest:
                second_largest = n
        
        if largest >= second_largest * 2:
            return index
        else: return -1
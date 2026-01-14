class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        left = 0
        right = len(arr)-1
        while left < right:
            if arr[left] != 0:
                left = left+1 # increment by 1 if not 0
            else:
                while left + 1 != right: # loop to replace values so that there is place to add 0
                    arr[right] = arr[right-1]
                    right = right - 1 # decrease by one to stop while loop
                arr[left+1] = 0
                left = left + 2
                right = len(arr)-1
        return arr

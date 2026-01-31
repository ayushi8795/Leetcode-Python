class Solution:
    def fixedPoint(self, arr: List[int]) -> int:

        def bin(firstoccur):
            l = 0
            h = len(arr)-1
            index = -1

            while l <= h:
                mid = (l+h)//2
                if arr[mid] == mid:
                    index = mid
                    if firstoccur:
                        h = mid-1
                elif arr[mid] < mid:
                    l = mid+1
                else:
                    h = mid -1
            return index

        ans = bin(True)
        return ans
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        left = 0
        right = len(arr) - 1

        while left <= right:
            pivot = (left+right)//2
            print((left,pivot,right))
            print(arr[pivot]-pivot-1)
            if arr[pivot]-pivot-1 < k:
                left = pivot +1
            else:
                right = pivot -1
        return left+k

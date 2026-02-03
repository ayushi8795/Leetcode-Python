class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr = heights[:]
        leng = len(arr)

        for i in range(leng):
            for j in range(0, leng - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        count = 0
        for i in range(len(arr)):
            print((heights[i],arr[i]))
            if heights[i] != arr[i]:
                count +=1
        return count
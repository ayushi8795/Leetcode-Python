class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        maxnum = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = maxnum
            if temp > maxnum:
                maxnum = temp
        return arr
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result =  []

        for i in range(len(arr)-1):
            nextnum = i+1
            result.append(max(arr[nextnum:]))
        result.append(-1)
        
        return result
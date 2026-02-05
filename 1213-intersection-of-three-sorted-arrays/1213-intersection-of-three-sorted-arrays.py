class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        result = []
        for each in arr1:
            arr2num = self.bin(each, arr2)
            arr3num = self.bin(each, arr3)
            if arr2num == arr3num and arr2num != -1 :
                result.append(each)
        return result

    
    def bin(self,target, arr):
        low = 0
        high = len(arr)-1

        while low <= high:
            mid  = (low+high)//2
            if arr[mid] == target:
                print(arr[mid])
                return arr[mid]
            elif arr[mid] < target:
                low = mid +1
            else:
                high = mid-1
        return -1
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:

        # for loop because it is already sorted so the 1st common found in all threee would be smallest 
        for i in range(len(mat[0])):
            target = mat[0][i]
            targetFound = [target]
            for j in range(1,len(mat)):
                returned = self.binsearch(mat[j],target)
                if returned == target:
                    targetFound.append(returned)
        
            if len(targetFound) == len(mat):
                return targetFound[0]
        return -1
    
    def binsearch(self,lis,target):
        low = 0
        high = len(lis)-1
        while low <= high:
            mid = (low+high)//2
            if lis[mid] == target:
                return target
            elif lis[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return -1
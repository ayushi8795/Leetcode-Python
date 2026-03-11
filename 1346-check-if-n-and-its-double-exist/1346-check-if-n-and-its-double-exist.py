class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count = {}

        for num in arr:
            if num not in count:
                count[num] = 1
            else:
                count[num]+=1
        
        for num in arr:
            if num != 0 and 2*num in count:
                return True
            
            if num == 0 and count[num] >1:
                return True 
        return False

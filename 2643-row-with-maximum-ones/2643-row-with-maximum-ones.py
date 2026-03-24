class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        lis = {}

        for row in range(len(mat)):
            count = 0
            for item in mat[row]:
                if item == 1:
                    count+=1
            if count != 0:
                lis[row] = count

        maxVal = -1
        keyIndex = -1
        for key,value in lis.items():
            if maxVal < value:
                maxVal = value
                keyIndex = key
        if keyIndex != -1:
            return [keyIndex,maxVal]
        else:
            return [0,0]

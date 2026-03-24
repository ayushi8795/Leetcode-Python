class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        lis = {}

        for row in range(len(mat)):
            count = 0
            # can use sum(mat[row]) as well.
            for item in mat[row]:
                if item == 1:
                    count+=1
            if count != 0:
                lis[row] = count

        maxVal = 0
        keyIndex = 0
        for key,value in lis.items():
            if maxVal < value:
                maxVal = value
                keyIndex = key

        return [keyIndex,maxVal]


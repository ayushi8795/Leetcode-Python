class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])
        r = n-1
        c = 0

        while r >= 0 and c < m:
            print(matrix[r][c])
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                c = c+1
            else:
                r = r-1
        return False
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_len = len(matrix)
        col_len = len(matrix[0])
        lucky = []

        # this finds min element in each row and stores at the ith location in list
        row_min = []
        for i in range(row_len):
            rMin = float('inf')
            for j in range(col_len):
                rMin = min(rMin, matrix[i][j])
            row_min.append(rMin)
        
        # this finds max element in each column and stores at the ith location in list
        col_max = []
        for i in range(col_len):
            cMax = float('-inf')
            for j in range(row_len):
                cMax = max(cMax,matrix[j][i])
            col_max.append(cMax)
        
        for r in range(row_len):
            for c in range(col_len):
                if matrix[r][c] == row_min[r] and matrix[r][c] == col_max[c]:
                    lucky.append(matrix[r][c])
        return lucky
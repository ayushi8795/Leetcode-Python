class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_len = len(grid)
        col_len = len(grid[0])
        one_Row_Arr = [0]*row_len
        one_col_Arr = [0]*col_len
        diff = [[0] * col_len for _ in range(row_len)]

        # calulate no of 1's in row
        for r in range(row_len):
            one_Row_Arr[r] = sum(grid[r])
        
        # calculate no of 1's in each column
        for c in range(col_len):
            x = 0
            for r in range(row_len):
                x += grid[r][c]
            one_col_Arr[c] = x
        print(one_Row_Arr)
        print(one_col_Arr)

        for r in range(row_len):
            for c in range(col_len):

                diff[r][c] = (one_Row_Arr[r] + one_col_Arr[c]) - (row_len - one_Row_Arr[r] + col_len - one_col_Arr[c])
        
        return diff
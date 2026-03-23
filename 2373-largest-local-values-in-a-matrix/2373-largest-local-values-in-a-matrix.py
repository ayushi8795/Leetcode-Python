class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        res = [[0]*(N-2)for _ in range(N-2)]

        for res_row in range(N-2):    #res_row = 0
            for res_col in range(N-2): #res_col = 0 
                for row in range(res_row,res_row+3):   # Hence, range is 0,3
                    for col in range(res_col,res_col+3): # Hence, range is 0,3
                        res[res_row][res_col] = max(res[res_row][res_col], grid[row][col])
        return res
        


        
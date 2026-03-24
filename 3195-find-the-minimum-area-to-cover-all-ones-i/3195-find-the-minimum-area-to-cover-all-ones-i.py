class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        # for finding the top boundry row value should be min. Hence n
        min_row = n
        # for finding the bottom boundry row value should be max. hence 0
        max_row = 0

        # for finding left boundry col_val should be min. hence n 
        min_col = m
        #for findng right boundry col_val should be max. hence 0
        max_col = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    min_row = min(r,min_row)
                    max_row = max(r, max_row)
                    min_col = min (c, min_col)
                    max_col = max(max_col,c)

        return (max_row-min_row+1)*(max_col-min_col+1)

        
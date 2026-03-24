class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.len = len(self.grid)

    def adjacentSum(self, value: int) -> int:
        adj_sum = 0
        for r in range(self.len):
            for c in range(self.len):
                if self.grid[r][c] == value:
                    if r-1 >=0:
                        adj_sum += self.grid[r-1][c]
                    if r+1 <= self.len-1:
                        adj_sum += self.grid[r+1][c]
                    if c+1 <= self.len-1:
                        adj_sum += self.grid[r][c+1]
                    if c-1 >=0:
                        adj_sum += self.grid[r][c-1]
                
        return adj_sum


    def diagonalSum(self, value: int) -> int:
        diag_sum =0

        for r in range(self.len):
            for c in range(self.len):
                if self.grid[r][c] == value:
                    if r-1 >=0 and c-1 >=0:
                        diag_sum += self.grid[r-1][c-1]
                    if r+1 <= self.len-1 and c-1 >=0 :
                        diag_sum += self.grid[r+1][c-1]
                    if c+1 <= self.len-1 and  r+1 <= self.len-1:
                        diag_sum += self.grid[r+1][c+1]
                    if c+1 <= self.len-1 and r-1 >=0:
                        diag_sum += self.grid[r-1][c+1]

        return diag_sum
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
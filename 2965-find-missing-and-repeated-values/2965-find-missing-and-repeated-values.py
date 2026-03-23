class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        Range = [1,n**2]
        ans=[0]*2
        visited = set()

        for row in range(n):
            for col in range(n):
                if grid[row][col] in visited:
                    ans[0] = grid[row][col]
                else:
                    visited.add(grid[row][col])

        for i in range(Range[0],Range[1]+1):
            if i not in visited:
                ans[1] = i
        return ans

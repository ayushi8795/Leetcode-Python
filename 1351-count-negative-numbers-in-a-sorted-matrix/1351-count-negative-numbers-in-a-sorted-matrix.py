class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        length = len(grid[0])
    
        for row in grid:
            low = 0
            high = length-1
            while low <= high:
                mid = (low+high)//2

                if row[mid] >= 0:
                    low = mid+1
                else:
                    high = mid-1
            count = count + (length-low)
        return count

                

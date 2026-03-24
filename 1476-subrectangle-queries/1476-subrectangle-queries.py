class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.row_len = len(self.rectangle)
        self.col_len = len(self.rectangle[0])
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:

        
        for r in range(self.row_len):
            for c in range(self.col_len):
                if row1 <= r <=row2 and col1 <= c <= col2:
                    self.rectangle[r][c] = newValue


    def getValue(self, row: int, col: int) -> int:
            return self.rectangle[row][col]
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
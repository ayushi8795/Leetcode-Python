class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        output =0 
        # since its a squar mat and primary diagonal is row == column

        for i in range(n):
            output+=mat[i][i]
            # secondary diagonal is [n-1-i]+[i] i.e. the total is indices would be equal to len of mat-1
            output+=mat[n-1-i][i]
            
        if n%2 != 0:
            output -= mat[n//2][n//2]
        return output


          
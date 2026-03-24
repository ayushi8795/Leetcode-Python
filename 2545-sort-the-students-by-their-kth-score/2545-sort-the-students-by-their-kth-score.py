class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score_len = len(score)
        
        for row_stu in range(score_len):
            # len(score-row_stu-1) reduces column by 1 because after every row_stud 1 row is solved and column is reduced.
            for col_exam in range(0, score_len-row_stu-1):
                if score[col_exam][k] < score[col_exam+1][k]:
                    score[col_exam],score[col_exam+1] = score[col_exam+1],score[col_exam]
            
        return score
    
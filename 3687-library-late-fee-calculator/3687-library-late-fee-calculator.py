class Solution:
    def lateFee(self, daysLate: List[int]) -> int:
        total = 0

        for num in daysLate:
            if num ==1:
                total = total + num
            elif 2 <= num <= 5:
                total = total + (2*num)
            else:
                total = total + (3*num)
        
        return total
            
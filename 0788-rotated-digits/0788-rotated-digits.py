class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid_same = {'0','1','8'}
        valid_change = {'2','5','6','9'}
        invalid = {'3','4','7'}

        count = 0

        for num in range(1, n+1):
            has_changed_digit = False
            is_valid = True

            for digit in str(num):
                if digit in invalid:
                    is_valid = False
                    break
                
                if digit in valid_change:
                    has_changed_digit = True
            if is_valid and has_changed_digit:
                count+=1
        return count
            

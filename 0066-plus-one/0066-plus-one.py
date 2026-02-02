class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numOfDigit = len(digits)
        for i in range(numOfDigit-1,-1,-1):
            if digits[i] == 9:
                 digits[i] = 0
            else:
                digits[i] = digits[i] +1
                return digits
        return [1] + digits
        
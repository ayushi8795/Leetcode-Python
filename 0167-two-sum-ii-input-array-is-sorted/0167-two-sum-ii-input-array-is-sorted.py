class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            sumNumber = numbers[left] + numbers [right]
            if sumNumber == target:
                return [left+1, right+1]
            elif sumNumber > target:
                right = right-1
            else:
                left = left +1
        
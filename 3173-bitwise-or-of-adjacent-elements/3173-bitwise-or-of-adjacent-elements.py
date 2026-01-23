class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range (1, len(nums)):
            answer.append(nums[i-1] | nums[i])
        return answer

        
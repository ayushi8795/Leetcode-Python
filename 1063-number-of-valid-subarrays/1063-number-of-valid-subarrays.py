class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for nu in nums:
            while stack and stack[-1] > nu:
                stack.pop()
            stack.append(nu)
            ans +=len(stack)
        return ans
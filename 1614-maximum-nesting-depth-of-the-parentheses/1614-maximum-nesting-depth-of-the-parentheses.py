class Solution:
    def maxDepth(self, s: str) -> int:
        maxCount = count= 0
        stack = []

        for i in s:
            if i == '(':
                stack.append(i)
                count = count+1
            elif i == ')':
                stack.pop()
                count = count -1
            maxCount = max(count, maxCount)
        return maxCount
        




class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in s:
            if len(stack) ==0:
                stack.append(i)
                continue
            
            if i == "B" and stack[-1] =="A":
                stack.pop()
            elif i == "D" and stack[-1] =="C":
                stack.pop()
            else:
                stack.append(i)
        return len(stack)
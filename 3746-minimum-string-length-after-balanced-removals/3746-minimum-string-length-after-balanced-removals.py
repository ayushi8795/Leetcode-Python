class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        stack = []


        for i in s:
            if not stack:
                stack.append(i)
            else:
                if i == "a" and stack[-1] =="b":
                    stack.pop()
                elif i == "b" and stack[-1] == "a":
                    stack.pop()
                else:
                    stack.append(i)

        return len(stack)
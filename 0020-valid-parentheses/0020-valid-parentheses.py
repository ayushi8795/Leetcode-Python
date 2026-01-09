class Solution:
    def isValid(self, s: str) -> bool:
        opens = ["(","[","{"]
        stack =[]

        for i in s:
            if i in opens:
                stack.append(i)
            elif stack:
                if ( i == ")" and stack[-1] == "(" ) or (i == "]" and stack[-1] == "[") or (i =="}" and stack[-1] == "{"):
                    stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0

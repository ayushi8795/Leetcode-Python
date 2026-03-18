class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        partLength = len(part)

        for char in s:
            stack.append(char)

            if len(stack) >= partLength:
                if "".join(stack[-partLength:]) == part:
                    i = 0
                    while i < partLength:
                        stack.pop()
                        i = i+1
        return "".join(stack)


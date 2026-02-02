import re
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for number in s:
            if re.search("[0-9]", number):
                stack.pop()
            else:
                stack.append(number)
        return "".join(stack)
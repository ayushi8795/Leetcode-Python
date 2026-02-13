class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == "]":
                newWords =""
                words = ""
                digit = ''
                while stack and stack[-1].isalpha():
                    words = stack.pop()+words
                if stack[-1] == "[":
                    stack.pop()
                while stack and stack[-1].isdigit():
                    digit = stack.pop()+digit
                newWords = int(digit)*words
                stack.append(newWords)
            else:
                stack.append(char)
        return "".join(stack)
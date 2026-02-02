class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            stack = []
            for ch in s:
                if ch != "#":
                    stack.append(ch)
                elif stack:
                    stack.pop()
                    
            return ''.join(stack)

        return build(s) == build(t)

        

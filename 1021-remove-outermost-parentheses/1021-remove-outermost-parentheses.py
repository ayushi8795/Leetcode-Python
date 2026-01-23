class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = ''
        temp = ''

        for ch in s:
            if ch =='(':
                stack.append(ch)
                temp+= '('
            elif ch ==')':
                stack.pop()
                temp+=')'
            
            if not stack:
                temp = temp[1:][:-1]
                ans+=temp
                temp =''
        return ans
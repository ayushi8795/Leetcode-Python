class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popPoint = 0

        stack = []

        for i in pushed:
            stack.append(i)

            while stack and popPoint < len(popped) and stack[-1] == popped[popPoint]:
                stack.pop()
                popPoint+=1
                
        return popPoint == len(popped)
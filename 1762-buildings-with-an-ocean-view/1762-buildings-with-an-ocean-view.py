class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []

        for index, value in enumerate(heights):
            while stack and stack[-1][1] <= value:
                stack.pop()
            stack.append([index,value])
        return [x[0] for x in stack]


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        
        for index,temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stktemp, stkInd = stack.pop()
                res[stkInd] = index - stkInd
            stack.append([temp,index])
        return res
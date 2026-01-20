class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = {}
        currmax = 0
        leftmostFruit =0
        for i in range(len(fruits)):
            if fruits[i] in dic:
                dic[fruits[i]] =dic[fruits[i]]+1
            else:
                dic[fruits[i]] =1
            
            while len(dic)>2:
                dic[fruits[leftmostFruit]] -=1
                if dic[fruits[leftmostFruit]] ==0:
                    del dic[fruits[leftmostFruit]] 
                leftmostFruit = leftmostFruit +1
            print(dic)
            currmax = max(currmax, i-leftmostFruit+1)
        return currmax
        
            
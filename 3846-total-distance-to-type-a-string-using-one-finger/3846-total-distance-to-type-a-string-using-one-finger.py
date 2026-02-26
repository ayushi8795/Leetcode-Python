class Solution:
    def totalDistance(self, s: str) -> int:
        Keyboard = [['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l'],['z','x','c','v','b','n','m']]

        dic = {}
        total = 0

        for row in range(len(Keyboard)):
            for column in range(len(Keyboard[row])):
                if column not in dic:
                    dic[Keyboard[row][column]] = (row,column)

        curr_r,curr_c = dic['a']
        
        for i in s:
            if i in dic:
                r, c = dic[i]
                total = total + abs(r-curr_r) + abs(c-curr_c)
                curr_r = r
                curr_c = c
        return total
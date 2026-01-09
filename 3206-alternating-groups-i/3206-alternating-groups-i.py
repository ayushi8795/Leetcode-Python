class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        left = 0
        dic = {0:1,1:0}
        count = 0
        n = len(colors)
        while 0 <= left <  n:
            if colors[(n+left-1)%n] == dic[colors[left%n]] and colors[(n+left+1)%n] == dic[colors[left%n]] :
                count = count + 1
            left = left +1
        return count

        
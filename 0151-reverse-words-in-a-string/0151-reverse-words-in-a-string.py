class Solution:
    def reverseWords(self, s: str) -> str:
        
        lis = s.split()
        start = 0
        end = len(lis)-1

        while start < end :
            lis[start],lis[end] = lis[end],lis[start]
            start +=1
            end-=1
        return " ".join(lis)
        
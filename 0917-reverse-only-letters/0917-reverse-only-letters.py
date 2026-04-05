class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        start = 0 
        end = len(s)-1
        k = list(s)

        while start < end:
            if not k[start].isalpha():
                start+=1
            if not k[end].isalpha():
                end-=1

            if k[start].isalpha() and k[end].isalpha():
                k[start],k[end] = k[end],k[start]
                start +=1
                end-=1
        return "".join(k)
        
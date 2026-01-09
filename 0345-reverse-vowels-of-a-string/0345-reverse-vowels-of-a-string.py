class Solution:
    def reverseVowels(self, s: str) -> str:
        lis = ['a','e','i','o','u',"A","E","I","O","U"]

        s=list(s)
        start = 0
        end = len(s)-1

        while start<end:
            if s[start] in lis and s[end] in lis:
                s[start],s[end]= s[end],s[start]
                start = start+1
                end = end-1
            elif s[start] in lis and s[end] not in lis:
                end = end-1
            elif s[start] not in lis and s[end] in lis:
                start = start +1
            else:
                start = start+1
                end = end-1
        return "".join(s)
                
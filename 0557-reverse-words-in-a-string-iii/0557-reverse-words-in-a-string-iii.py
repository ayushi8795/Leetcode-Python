class Solution:
    def reverseWords(self, s: str) -> str:
        strList = s.split()
        newstr = []

        for eachstr in strList:
            eachstr = list(eachstr)
            start = 0
            end = len(eachstr)-1
            while start < end:
                eachstr[start],eachstr[end] = eachstr[end],eachstr[start]
                start = start + 1
                end = end - 1
            newstr.append("".join(eachstr))
        return " ".join(newstr)


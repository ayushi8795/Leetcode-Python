class Solution:
    def reverse(self, x: int) -> int:

        x= list(str(x))

        start = 0
        end = len(x)-1

        while start < end:

            if x[start] == '-':
                start = start+1
            x[start],x[end]=x[end],x[start]
            start = start+1
            end = end-1

        y = int("".join(x))

        if pow(-2,31) <= y<= pow(2,31)-1:
            return y
        else:
            return 0
        
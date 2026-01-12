class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        start = 0
        end = k-1
        s = list(s)

        while start < end:
            s[start],s[end] = s[end],s[start]
            start = start + 1
            end = end -1
        return ''.join(s)
        
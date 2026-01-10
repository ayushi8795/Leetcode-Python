class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        need = len(needle)
        
        while i < len(haystack):
            if haystack [i: i+need] == needle:
                return i
            i = i+1
        return -1

        
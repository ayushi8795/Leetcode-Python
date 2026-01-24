class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strArr = s.split()
        return len(strArr[-1])
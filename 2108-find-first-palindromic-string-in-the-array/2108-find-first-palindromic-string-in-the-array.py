class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        for word in words:
            if self.pali(word):
                return word
        return ""
    
    def pali(self,word):
        start = 0
        end = len(word)-1
        while start <= end:
            if word[start] != word[end]:
                return False
            else:
                start = start +1
                end = end-1
        return True
            
        
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        word1 = list(word1)
        word2 = list(word2)
        newword = ''

        i =0
        while i <= len(word1)-1 and i <= len(word2)-1:
            newword = newword + word1[i] + word2[i]
            i = i +1
        
        if len(word1) < len(word2):
            newword = newword + ''.join(word2[i:])
        else:
            newword = newword + ''.join(word1[i:])
        
        return newword


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text_lis = text.split(" ")
        broken_set = set(brokenLetters)
        count =0
        
        for i in text_lis:
            for c in i:
                if c in broken_set:
                    count = count+1
                    break
        return len(text_lis)-count
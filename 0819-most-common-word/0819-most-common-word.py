class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        wordDic = {}
        for char in paragraph:
            if not char.isalnum():
                paragraph = paragraph.replace(char, " ")
        paragraph = paragraph.lower().split()
    
        for i in paragraph:
            if i not in banned and i.isalnum():
                if i not in wordDic.keys():
                    wordDic[i] = 1
                else:
                    wordDic[i] = wordDic[i]+1
        print(wordDic)
        maxVal = max(wordDic.values())
        for key, value in wordDic.items():
            if value == maxVal:
                return key
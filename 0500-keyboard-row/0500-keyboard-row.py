class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        set1 = {'q','w','e','r','t','y','u','i','o','p'}
        set2  ={'a','s','d','f','g','h','j','k','l'}
        set3 = {'z','x','c','v','b','n','m'}

        res = []

        for wor in words:
            wordset = set(wor.lower())

            # Here A&B is the intersection of two sets and then checking if it is same to wordset meaning all word exsists in the same row
            if (wordset&set1==wordset or wordset&set2==wordset or wordset&set3==wordset):
                res.append(wor)
        return res
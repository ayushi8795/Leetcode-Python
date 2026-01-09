class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        left = 0

        while left+3 <len(s)+1:
            dic = {}
            for i in range(left, left+3):
                if s[i] not in dic.keys():
                    dic[s[i]] = 1
                else:
                    # dic[s[i]] = dic[s[i]]+1
                    break
            
            left = left + 1
            print(dic)
            if len(dic) == 3:
                res =res+1
            print(res)

        return res


        
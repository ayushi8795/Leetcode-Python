class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        hashnum = {}
        if len(nums) <=2:
            return max(nums)
        for i in nums:
            if i not in hashnum:
                hashnum[i] = 1
            else:
                hashnum[i]+=1
        dic = sorted(hashnum.items(), key= lambda item : item[0], reverse=True)
        keyList = [key for key,value in dic]
        if len(keyList) >= 3:
            return keyList[2]
        else:
            return max(keyList)
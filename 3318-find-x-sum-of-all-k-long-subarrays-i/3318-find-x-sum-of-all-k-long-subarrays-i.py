class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        n = len(nums)
        i =0
        
        for start in range(n-k+1):
            dic = {}
            for i in range(start,start+k):
                if nums[i] not in dic:
                    dic[nums[i]] = 1
                else:
                    dic[nums[i]] +=1
            fre = sorted(dic.items(), key = lambda item: (-item[1], -item[0]))
            s = 0
            for key,value in fre[:x]:
                s = s + (key*value)
            ans.append(s)
        return ans
            
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        dic = defaultdict(int)

        for i in nums:
            ans = ans+dic[i]
            dic[i]+=1
        return ans
                
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res =[]
        sortedNum = sorted(nums)
        hashi ={}

        for i in range(len(sortedNum)):
            if sortedNum[i] not in hashi:
                hashi[sortedNum[i]] = i
        
        for i in nums:
            res.append(hashi[i])
        return res

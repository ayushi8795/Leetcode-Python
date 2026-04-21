class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        hashi = {}
        count = 0

        for i in nums:
            if i not in hashi:
                hashi[i] = 1
            else:
                hashi[i] +=1
        
        max_freq = max(hashi.values())

        for key,value in hashi.items():
            if value == max_freq:
                count = count + value
        return count
        
        
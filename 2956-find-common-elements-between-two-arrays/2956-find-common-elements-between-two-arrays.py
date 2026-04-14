class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans1_freq = {}
        ans2_freq = {}

        for i in nums1:
            if i in nums2:
                if i not in ans1_freq:
                    ans1_freq[i] = 1
                else:
                    ans1_freq[i] = ans1_freq[i] + 1
        
        for j in nums2:
            if j in ans1_freq:
                if j not in ans2_freq:
                    ans2_freq[j] = 1
                else:
                    ans2_freq[j] = ans2_freq[j] +1
        return [sum(ans1_freq.values()), sum(ans2_freq.values())]
        
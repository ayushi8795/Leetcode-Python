class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nu1 = set()
        nu2 = set()

        for n in nums1:
            if n not in nums2:
                nu1.add(n)
        for n in nums2:
            if n not in nums1:
                nu2.add(n)
        return [list(nu1),list(nu2)]


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp = []
        num2_hash = {}

        for index, value in enumerate(nums2):
            num2_hash[value] = index

        for i in nums1:
            mapp.append(num2_hash[i])
        return mapp

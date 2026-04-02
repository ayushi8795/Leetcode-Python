class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        kmultiplier = {}
        count = 0

        for index, nu in enumerate(nums2):
            kmultiplier[index] = nu*k
        

        for key, value in kmultiplier.items():
            for n in nums1:
                if n%value == 0:
                    count = count+1
        return count 
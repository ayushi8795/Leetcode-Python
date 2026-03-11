class Solution:
    def minimumSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        pos1 = {}
        minva = -1

        for index, nu in enumerate(nums1):
            if nu not in pos1:
                pos1[nu] = index
            else:
                if pos1[nu] > index:
                    pos1[nu] = index

        for j in range(len(nums2)):
            if pos1 and nums2[j] in pos1:
                total = j + pos1[nums2[j]]

                if minva == -1:
                    minva = total
                else:
                    minva = min(minva,total)
        return minva


            

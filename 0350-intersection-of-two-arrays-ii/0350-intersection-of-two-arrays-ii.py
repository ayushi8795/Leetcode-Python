class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            seen = enumerate(nums1)
            result = self.check(seen,nums2)
        else:
            seen = enumerate(nums2)
            result = self.check(seen,nums1)
        return result

    def check(self,seendic,num):
        result = []
        temp = -1
        lenofnum = len(num)
        
        for index, value in seendic:
                if value in num:
                    result.append(value)
                    num[num.index(value)] = -1
        return result


        
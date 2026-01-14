class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dic = {}

        for n in range(len(nums)):
            if nums[n] != 0:
                self.dic[n] = nums[n]
    
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        summ = 0
        print(self.dic)
        print(vec.dic)

        for key in self.dic.keys():
            if key in vec.dic.keys():
                summ = summ + (self.dic[key] * vec.dic[key])
        return summ
        
        


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
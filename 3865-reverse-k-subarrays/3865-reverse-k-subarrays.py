class Solution:
    def reverseSubarrays(self, nums: list[int], k: int) -> list[int]:

        sizeEachArr = len(nums)//k
        
        for beg in range(0,len(nums),sizeEachArr):
            nums[beg:beg+sizeEachArr] = nums[beg:beg+sizeEachArr][::-1]
        return nums
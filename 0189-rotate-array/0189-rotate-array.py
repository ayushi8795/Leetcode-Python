class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = k
        n = len(nums)

        while 0<count <= k:
            nums.insert(0,nums[-1])
            del nums[-1]
            count -=1
        return nums
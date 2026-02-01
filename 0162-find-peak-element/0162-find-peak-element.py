class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return 0
        if len(nums) <3:
            if nums[0] < nums[1]:
                return 1
            else:
                return 0

        l = 0
        h = len(nums)-1
        while l < h:
            mid = (l+h)//2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                h = mid-1
        return l
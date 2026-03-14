class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        poscount = len(nums)-self.upper_bound(nums)
        negcount = self.lower_bound(nums)
        return max(poscount,negcount)
    # Lower bound means last index of 0 or 1st index positive number
    def lower_bound(self,nums):
        low = 0
        high = len(nums)-1
        index = len(nums) # means there is no 0 or no positive number
        while low <= high:
            mid = (low+high)//2

            if nums[mid] < 0:
                low = mid +1
            else:
                high = mid-1
                index = mid
        return index 

    # Upper bound means  first index of 0 or last index of negative number
    def upper_bound(self, nums):
        low = 0
        high = len(nums)-1
        index = len(nums)

        while low<=high:
            mid = (low+high)//2

            if nums[mid] <= 0:
                low = mid+1
            else:
                high = mid-1
                index = mid
        return index 


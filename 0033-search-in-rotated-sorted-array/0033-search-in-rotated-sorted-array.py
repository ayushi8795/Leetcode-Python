class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        low = 0 
        high = n-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] > nums[-1]:
                low = mid+1
            else:
                high = mid -1 
        

        def bin(lower, upper, target):

            while lower <= upper:
                mid = (lower+upper)//2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    upper = mid -1 
                else:
                    lower = mid +1
            return -1

        # searching from left to pivot
        left_subarry = bin(0,low -1, target)
        if left_subarry !=-1:
            return left_subarry
        
        #searching from pivot to right:
        right_subarray = bin(low, n-1, target)
        return right_subarray

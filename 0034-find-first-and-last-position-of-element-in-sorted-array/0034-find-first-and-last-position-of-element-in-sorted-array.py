class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # low = 0 
        # high = len(nums)-1
        # Range = []

        # def binarySearch(low,high,Range):
        #     while low < high:
        #         mid = (low+high)//2
        #         if nums[mid] == target:
        #             Range.append(mid)
        #         elif nums[mid] < target:
        #             return binarySearch(mid + 1,high,Range)
        #         else:
        #             return binarySearch(low,mid-1,Range)
        
        # return [-1,-1] if len(Range) == 0 else Range

        def bin(target, first_index):
            low = 0 
            high = len(nums)-1
            pos = -1
            while low <= high:
                mid = (low+high)//2

                if nums[mid] == target:
                    pos = mid

                    if first_index:
                        high = mid -1
                    else:
                        low = mid+1
                elif nums[mid] > target:
                    high = mid -1
                else:
                    low = mid +1
            return pos

        first = bin(target, first_index = True)
        last = bin(target, first_index= False)
        return [first, last]



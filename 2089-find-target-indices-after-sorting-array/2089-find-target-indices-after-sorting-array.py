class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        def binsearch(target, find_first):

            left = 0
            right = len(nums)-1
            pos = -1

            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    pos = mid
                    if find_first:
                        right = right-1
                    else:
                        left = left +1
                elif nums[mid] > target:
                    right = right -1
                else:
                    left = left+1
            return pos
        # searching left half
        left = binsearch(target, find_first = True)
        if left == -1:
            return []

        # sarching right half
        right = binsearch(target, find_first = False)
        return list(range(left,right+1))

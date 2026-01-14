class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        count = 0

        while l<= r:
            if nums[l] != val:
                l = l+1
                count +=1
            else:
                if nums[r] != val:
                    nums[l], nums[r] = nums[r], nums[l]
                    count+=1
                    l =l +1
                    r = r-1
                else:
                    r = r-1
        return count
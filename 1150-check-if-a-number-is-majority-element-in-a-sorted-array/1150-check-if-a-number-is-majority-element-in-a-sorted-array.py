class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        

        def bin(target, first_occur):
            l = 0
            h = len(nums)-1
            pos = -1

            while l <=h:
                mid =(l+h)//2

                if nums[mid] == target:
                    pos = mid
                    if first_occur:
                        h = mid-1
                    else:
                        l = mid+1
                elif nums[mid] > target:
                    h = mid -1
                else:
                    l = mid+1
            return pos
                

        first = bin(target, first_occur= True)
        last = bin(target, first_occur= False)

        if first != -1 and last != -1 and (last-first+1) > (len(nums)/2):
            return True
        else:
            return False
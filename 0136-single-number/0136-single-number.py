class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        notDuplicate = []
        for i in nums:
            if i not in notDuplicate:
                notDuplicate.append(i)
            else:
                notDuplicate.remove(i)
        return notDuplicate.pop()

                 

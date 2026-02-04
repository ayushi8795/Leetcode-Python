class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        greaterMap = {}
        stack = []
        
        for eachNum in nums2:
            while stack and eachNum > stack[-1]:
                greaterMap[stack.pop()] = eachNum
            stack.append(eachNum)
        return [greaterMap.get(i,-1) for i in nums1]
        

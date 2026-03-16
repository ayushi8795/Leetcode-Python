class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        left,right,count = {},{},{}

        for index, nu in enumerate(nums):
            if nu not in left:
                left[nu] = index
            '''this is done because if element is only present 1 time left == right.
            Not checking if element in right we are constantly updating right index
            as we are finding element. '''
            right[nu] = index
            count[nu] = count.get(nu,0)+1
        ans = len(nums)
        degree = max(count.values())

        for x in count:
            if count[x] ==degree:
                ans = min(ans,right[x]-left[x]+1)
        return ans
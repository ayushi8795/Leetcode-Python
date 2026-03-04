# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(low, high):
            if low > high:
                return None 
            mid = low + (high - low) // 2
            rootNode = TreeNode(nums[mid])
            rootNode.left = helper(low ,mid -1)
            rootNode.right = helper(mid+1, high)
            return rootNode

        return helper(0, len(nums)-1)

        



            
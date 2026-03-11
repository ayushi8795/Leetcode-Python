# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        root = None

        return self.construct(nums)

    def construct (self, nums):

        if not nums:
            return None
        nodeVal = max(nums)
        nodeIndex = nums.index(nodeVal)
        root = TreeNode(nodeVal)
        root.left = self.construct(nums[:nodeIndex])
        root.right = self.construct(nums[nodeIndex+1 :])
        return root

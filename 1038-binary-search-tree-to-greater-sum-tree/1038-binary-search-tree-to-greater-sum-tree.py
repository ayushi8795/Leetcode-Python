# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        total = 0
        self.convert(root, total)
        return root

    def convert(self,root,total):
        if not root:
            return total
            
        total = self.convert(root.right,total)
        total = total+root.val
        root.val = total
        total = self.convert(root.left, total)
        return total


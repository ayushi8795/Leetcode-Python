# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0
        else:
            stack = []
            self.call(root, stack)
            return sum(stack)
    
    def call(self,root,stack):
        xyz = float('inf')
        if root:
            if root.left:
                xyz = self.call(root.left,stack)
                if not root.left.left and not root.left.right:
                    stack.append(xyz)
            if root.right:
                self.call(root.right, stack)
        return root.val
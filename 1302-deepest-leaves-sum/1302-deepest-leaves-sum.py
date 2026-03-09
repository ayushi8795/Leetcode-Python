# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        depth = 0
        depth = self.depth(root,depth)
        total = self.calSum(root, depth, 0)

        return total

    def depth(self,root,depth):
        if not root:
            return depth
        return (1+max(self.depth(root.right,depth),self.depth(root.left,depth)))

    def calSum(self,root,depth,total):
        if root:
            total = self.calSum(root.left, depth-1, total)
            total= self.calSum(root.right, depth-1, total)

            if depth == 1:
                total = total + root.val
        return total

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        summation = 0
        if not root:
            return summation
        if root.val%2 == 0:
            if root.left:
                if root.left.left:
                    summation = summation + root.left.left.val
                if root.left.right:
                    summation = summation + root.left.right.val
            if root.right:
                if root.right.left:
                    summation = summation + root.right.left.val
                if root.right.right:
                    summation = summation + root.right.right.val

        summation = summation + self.sumEvenGrandparent(root.left)
        summation = summation + self.sumEvenGrandparent(root.right)
        
        return summation
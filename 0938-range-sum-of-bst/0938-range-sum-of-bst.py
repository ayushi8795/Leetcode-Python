# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summation = 0

        def help(root,summ):
            if root:
                if low <= root.val <= high:
                    summ= summ + root.val
                if root.left:
                    summ = help(root.left,summ)
                if root.right:
                    summ = help(root.right,summ)
            return summ

        return help(root,summation)

    

        
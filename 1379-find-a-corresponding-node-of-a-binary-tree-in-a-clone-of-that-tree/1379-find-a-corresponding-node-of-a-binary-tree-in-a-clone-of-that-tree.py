# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def helpInorder(ori,clo):
            if ori:
                helpInorder(ori.left,clo.left)
                if ori.val == target.val:
                    self.ans = clo
                helpInorder(ori.right,clo.right)
        helpInorder(original,cloned)
        return self.ans
                
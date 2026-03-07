# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0

        self.change(root.left, root.right, level)

        return root

    def change(self, left, right, level):
        if right is None or left is None:
            return
        print(level)
        if level%2 == 0:
            # to change the right and left child it needs to be done at one level above not at the same level. hence, ==0
            left.val, right.val = right.val, left.val 

        self.change(left.left, right.right, level+1)
        self.change(left.right, right.left, level+1)

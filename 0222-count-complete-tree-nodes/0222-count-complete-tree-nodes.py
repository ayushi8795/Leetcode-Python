# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0 

        if not root:
            return count 
        else:
            return self.count(root,count)

    def count(self,root,count):
        if root:
            count = count+1
            if root.left:
                count = self.count(root.left,count)
            if root.right:
                count = self.count(root.right,count)
        return count
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        sta = []

        def dfs(root1):
            if root1:
                sta.append(root1.val)
                dfs(root1.left)
                dfs(root1.right)
        dfs(root)
        return len(set(sta)) == 1            
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1lis = []
        root2lis = []

        self.traverse(root1, root1lis)
        self.traverse(root2, root2lis)

        return root1lis == root2lis
    
    def traverse(self, root, rootlis):
        if root:
            if root.left:
                self.traverse(root.left, rootlis)
            if root.right:
                self.traverse(root.right, rootlis)

            if not root.left and not root.right:
                return rootlis.append(root.val)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder = []
        inorder = self.inorder(root, inorder)
        return self.helper(inorder, 0, len(inorder)-1)

    def helper(self,inorder, low,high):
        if low > high:
            return None
        mid = (low+high)//2

        left_tree = self.helper(inorder,low, mid-1)
        right_tree = self.helper(inorder, mid+1, high)

        node = TreeNode(inorder[mid],left_tree,right_tree)

        return node

    def inorder(self, root, lis):
        if root:
            lis = self.inorder(root.left, lis)
            lis.append(root.val)
            lis = self. inorder(root.right, lis)
        return lis

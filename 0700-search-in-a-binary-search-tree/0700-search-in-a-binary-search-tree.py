# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root.val == val:
            print(root)
            return root
        elif root.left is not None and root.val > val:
            print("a",root.left)
            return self.searchBST(root.left,val)
        elif root.right is not None and root.val < val:
            print("b",root.left)
            return self.searchBST(root.right,val)
        else:
            return
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        return self.construct(root)

    def construct(self,root):

        if not root:
            return ""

        # Case 1: Leaf Node
        if not root.left and not root.right:
            return str(root.val)
        
        #Case 2: Only leaf child 
        if root.left and not root.right:
            return str(root.val) + "(" + self.construct(root.left) +")"
        
        #Case 3: right child exist 
        if not root.left and root.right:
            return str(root.val) + "()" + "(" + self.construct(root.right)+ ")"
        
        #Case 4: both children present:

        return (str(root.val)+"("+ self.construct(root.left)+")"+"("+ self.construct(root.right)+")")

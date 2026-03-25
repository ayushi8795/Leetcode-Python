# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            if root.val == 0:
                return False
            else:
                return True
        
        eval_left = self.evaluateTree(root.left)
        eval_right = self.evaluateTree(root.right)

        if root.val == 2:
            eval_root = eval_left or eval_right
        else:
            eval_root = eval_left and eval_right
            
        return eval_root
    

            
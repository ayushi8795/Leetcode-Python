# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        
        self.dfs(root)
        return self.count

    def dfs(self,root):
            if not root:
                return True
            
            count_left = self.dfs(root.left)
            count_right = self.dfs(root.right)

            if count_left and count_right:
                if root.left and root.val != root.left.val:
                    return False

                if root.right and root.val != root.right.val:
                    return False

                self.count+=1
                return True
            return False

                
                
            


            
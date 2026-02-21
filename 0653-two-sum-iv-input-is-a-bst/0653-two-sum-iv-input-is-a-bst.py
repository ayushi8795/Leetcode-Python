# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.completeTreeTraverse(root,root,k)

    def completeTreeTraverse(self,currNode, full_tree, k):
        if not currNode:
            return False
    
        value = k - currNode.val
        
        if self.findValue(currNode,value,full_tree):
            return True
        
        return self.completeTreeTraverse(currNode.left,full_tree,k) or self.completeTreeTraverse(currNode.right,full_tree,k)
        
    def findValue(self, currNode, value,full_tree):

        if full_tree:
            if full_tree.val == value and full_tree is not currNode:
                return True
            elif full_tree.val < value:
                return self.findValue(currNode, value,full_tree.right)
            else:
                return self.findValue(currNode, value,full_tree.left)
        return False
        
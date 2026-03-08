# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        diff= float('inf')
        minVal = float('inf')
        
        diff, val = self.traverse(root,target, diff, minVal)
        
        return val
        
    def traverse(self,root,target, diff,minVal):
        if root:
            if diff > abs(root.val-target):
                diff = abs(root.val-target)
                minVal = root.val
            elif diff == abs(root.val-target):
                diff = abs(root.val-target)
                if minVal > root.val:
                    minVal = root.val
                    
            diff,minVal=self.traverse(root.left,target,diff,minVal)
            diff,minVal=self.traverse(root.right,target,diff,minVal)


        return [diff,minVal]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        if root1:
            newTarget = target-root1.val
            Is2Node = self.find2Node(root2, newTarget)
            if not Is2Node and root1.left:
                Is2Node =self.twoSumBSTs(root1.left, root2, target)
            if not Is2Node and root1.right:
                Is2Node =self.twoSumBSTs(root1.right, root2,target)
        return Is2Node
    
    def find2Node(self, root2, target):
        IsNode = False
        if root2:
            if root2.val == target:
                IsNode = True
            elif root2.val < target:
                IsNode =self.find2Node(root2.right, target)
            else:
                IsNode= self.find2Node(root2.left, target)
        return IsNode


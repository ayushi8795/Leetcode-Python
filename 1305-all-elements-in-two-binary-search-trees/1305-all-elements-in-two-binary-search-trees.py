# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        lis1 = []
        lis2 = []

        lis1 = self.traverse(root1, lis1)
        lis2 = self.traverse(root2, lis2)

        print("lis1",lis1)
        print("lis2",lis2)

        lis1.extend(lis2)
        lis1.sort()
        return lis1


    def traverse(self, root, lis):
        if root:
            if root.left:
                lis = self.traverse(root.left, lis)
            lis.append(root.val)
            if root.right:
                lis = self.traverse(root.right, lis)
        return lis
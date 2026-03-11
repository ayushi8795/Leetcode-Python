# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

        if self.root:
            self.root.val = 0
            self.change(self.root)

    def find(self, target: int) -> bool:

        return self.findagain(self.root, target)
        
    def findagain(self, root, target):
        result = False

        if root:
            if root.val == target:
                return True
            if root.left:
                result = self.findagain(root.left,target)
            if not result and self.root.right:
                result = self.findagain(root.right,target)
        return result
    
    def change(self,root):
        if not root:
            return
        
        if root.left:
            root.left.val = 2*root.val+1
            self.change(root.left)


        if root.right:
            root.right.val = 2*root.val+2
            self.change(root.right)



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
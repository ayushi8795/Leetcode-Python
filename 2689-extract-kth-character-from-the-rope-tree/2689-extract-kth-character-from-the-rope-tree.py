# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """

        def dfs(root):
            if not root:
                return ''
            left_Str =  dfs(root.left)
            right_str = dfs(root.right)

            return left_Str + root.val + right_str
        string = dfs(root)

        return string[k-1]
            

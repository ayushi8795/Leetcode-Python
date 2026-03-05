# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        que = []
        res = []
        curr_level = 0

        que.append(root)

        while que:
            len_q = len(que)
            res.append([])
            for i in range(len_q):
                node = que.pop(0)
                res[curr_level].append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            curr_level+=1

        
        return res[::-1]

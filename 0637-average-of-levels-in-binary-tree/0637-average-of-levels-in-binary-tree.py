# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root:
            return 
        curr_level = 0
        que = []
        res = []
        que.append(root)

        while que:
            len_q = len(que)
            level_sum  = 0
    
            for _ in range(len_q):
                node = que.pop(0)
                level_sum+= node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            curr_level +=1

            res.append(level_sum/len_q)
        return res



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        res = []
        queTrack = []
        curr_level=0 
        queTrack.append(root)
        
        
        while queTrack:
            res.append([])
            len_q = len(queTrack)
            for i in range(len_q):
                node = queTrack.pop(0)
                res[curr_level].append(node.val)
                
                if node.left is not None:
                    queTrack.append(node.left)
                if node.right is not None:
                    queTrack.append(node.right)
            curr_level = curr_level+1
        return res
            
            
            
                
                
        
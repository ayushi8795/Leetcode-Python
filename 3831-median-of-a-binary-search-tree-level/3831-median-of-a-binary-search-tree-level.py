# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelMedian(self, root: Optional[TreeNode], level: int) -> int:
        que = []
        curr_level = 0
        que.append(root)
        res = []

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
            curr_level +=1

        if len(res) > level:
            len_res = len(res[level])
            l =0
            r = len_res-1
            mid = (l+r)//2

            if len_res%2 == 0:
                return res[level][mid+1]
            else:
                return res[level][mid]
        else:
            return -1
            



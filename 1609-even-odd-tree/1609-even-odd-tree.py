# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        que = []
        curr_level = 0
        que.append(root)

        while que:
            len_q = len(que)

            if curr_level%2==0:
                prev = float("-inf")
            else:
                prev = float("inf")

            for _ in range(len_q):
                node = que.pop(0)
                v = node.val
                
                if curr_level%2 == 0:
                    # Level is even so value should be odd and increasing
                    if v%2 ==0 or v <= prev:
                        return False
                else:
                    # Level is odd so value should even and decreasing
                    if v%2 ==1 or v >= prev:
                        return False
                
                # can assign directly because in for loop on same level
                prev = v

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            curr_level+=1
        return True
    
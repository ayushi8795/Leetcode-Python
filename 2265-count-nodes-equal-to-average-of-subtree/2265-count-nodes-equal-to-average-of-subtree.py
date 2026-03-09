# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        nodecount = 0
        total = 0
        total,nodecount, count = self.count(root,count,nodecount,total)

        return count

    def count(self, root, count,nodecount, total):
        if not root:
            return 0,0,0
        totalleft,nodecountleft,countleft =self.count(root.left,count,nodecount,total)
        totalright,nodecountright,countright =self.count(root.right,count,nodecount,total)

        total = totalleft + totalright + root.val
        nodecount = nodecountleft+nodecountright+1

        count = countleft+countright
        if int(total/nodecount) == root.val:
            count = count+1

        return total,nodecount,count
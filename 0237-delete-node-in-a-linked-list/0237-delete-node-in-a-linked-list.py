# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # I this case head is not given but the node is already idenitfied to be delte hence shift/overrisde the value of the next node and then delete next node
        
        node.val = node.next.val
        node.next = node.next.next

        
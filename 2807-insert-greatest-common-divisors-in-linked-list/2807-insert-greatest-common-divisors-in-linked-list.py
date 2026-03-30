# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def cal_gcd(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        
        if not head.next:
            return head

        node1 = head
        node2 = head.next

        while node2:
            gcVal = cal_gcd(node1.val,node2.val)
            gcNode = ListNode(gcVal)

            node1.next = gcNode
            gcNode.next = node2

            node1 = node2
            node2 = node2.next
        return head
        
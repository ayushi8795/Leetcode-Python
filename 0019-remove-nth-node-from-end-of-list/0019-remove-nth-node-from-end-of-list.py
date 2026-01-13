# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        mainPtr = refPtr = head 

        # Move refPtr ahead by n steps
        for _ in range(0, n):
            refPtr = refPtr.next
        
        # ref pointer reached the eand then n == length of list 
        if refPtr is None:
            return head.next

        #  Move both pointer till reference pointer reaches last node 
        while refPtr.next is not None:
            refPtr = refPtr.next 
            mainPtr = mainPtr.next

        mainPtr.next = mainPtr.next.next
        return head

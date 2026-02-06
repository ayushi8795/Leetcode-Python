# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # if head is val:
        while head and head.val == val:
            head = head.next
        
        #If list is empty
        if head is None:
            return head
        
        # all other case
        curr = head

        while curr:
            if curr.next and curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

        
            
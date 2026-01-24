# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentPointer = head   #current pointer is required because head cannot be moved
        while currentPointer is not None and currentPointer.next is not None:
            if currentPointer.val == currentPointer.next.val:
                currentPointer.next = currentPointer.next.next
            else:
                currentPointer = currentPointer.next
        return head

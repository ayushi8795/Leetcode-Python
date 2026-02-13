# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not head or head.next is None:
            return head
        elif head and head.next:
            first = head
            second = head.next 
            
            first.next = self.swapPairs(second.next)
            second.next= first
            return second
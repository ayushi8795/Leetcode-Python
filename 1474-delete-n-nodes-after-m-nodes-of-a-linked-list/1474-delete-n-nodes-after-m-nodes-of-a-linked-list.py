# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        current = last = head
        
        while current is not None:
            countm = countn = 1
            while current is not None and countm <= m:
                last = current
                current = current.next 
                countm = countm+1

            while current is not None and countn <= n:
                current = current.next
                countn = countn + 1
            last.next = current

        return head
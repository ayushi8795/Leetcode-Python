# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            upCommingNode = curr.next # store future node
            curr.next = prev # Point current node next to prev node to change order
            prev = curr # increment previous pointer by 1 to have the latest previous node
            curr = upCommingNode # futurenode becomes current node on which next execution will happen
        return prev
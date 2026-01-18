# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxVal = 0

        endoffirst = self.endoffirsthalf(head)
        firsthalfHead = head
        secondhalfreversed = self.reverse(endoffirst.next)

        # print(endoffirst)
        # print(secondhalfreversed)

        while firsthalfHead and secondhalfreversed:
            maxVal = max(maxVal, firsthalfHead.val+secondhalfreversed.val)
            firsthalfHead = firsthalfHead.next
            secondhalfreversed = secondhalfreversed.next
        return maxVal

    def endoffirsthalf(self,head):
        slow = fast= head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            node = curr.next
            curr.next = prev
            prev = curr
            curr = node
        return prev
    
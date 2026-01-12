# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        end_of_first_half = self.findfirsthalf(head)
        reverseof_second_half = self.reverse(end_of_first_half.next)

        result = True
        firstListPosition = head
        secondListPosition = reverseof_second_half

        while result and secondListPosition is not None:
            if firstListPosition.val != secondListPosition.val:
                result = False
            secondListPosition = secondListPosition.next
            firstListPosition = firstListPosition.next
        return result


    def reverse(self,head):
        prev = None
        curr = head
        while curr is not None:
            nextNode = curr.next 
            curr.next = prev 
            prev = curr
            curr = nextNode
        return prev
    
    def findfirsthalf(self,head):
        slow = fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

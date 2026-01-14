# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head
        index = 1
# we are counting the length of the linkedList as well
        while curr:
            # got the node at kth position
            if index == k:
                frontNode = curr
            curr = curr.next
            index = index +1
        endNodeIndex = index - k
        print(endNodeIndex)

        count = 1
        curr = head
        while curr:
            if count == endNodeIndex:
                endNode = curr
                break
            else:
                curr = curr.next
                count = count +1
        frontNode.val , endNode.val = endNode.val, frontNode.val
        return head

        

            

        
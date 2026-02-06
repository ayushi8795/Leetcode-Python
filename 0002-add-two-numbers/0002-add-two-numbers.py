# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        def getNumber(lis):
            numl = ''
            while lis != None:
                numl =  str(lis.val)+ numl
                lis = lis.next
            return int(numl)

        final = str(getNumber(l1) + getNumber(l2))
        final = final[::-1]

        dummyHead = ListNode(0)
        head = dummyHead
        for i in range(len(final)):
            x = int(final[i])
            newNode = ListNode(x)
            dummyHead.next = newNode
            dummyHead = newNode
        return head.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        frequency = {}
        current = head
        frequencyHead = None

        while current is not None:
            if current.val not in frequency:
                # Node banakar pura node hi as a value save kiya and head to adjust kiya recently added node pe 
                new_node = ListNode(1,frequencyHead)
                frequency[current.val] = new_node
                frequencyHead = new_node
            else:
                node = frequency[current.val]
                node.val += 1
            current = current.next
        return frequencyHead
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        oddTeamCounter = evenTeamCounter = 0
        currentPointer = head

        while currentPointer is not None:
            if currentPointer.val > currentPointer.next.val:
                evenTeamCounter = evenTeamCounter + 1
                print("evenTeamCounter : {}", evenTeamCounter)
            else:
                oddTeamCounter = oddTeamCounter + 1
                print("oddTeamCounter : {}", oddTeamCounter)
            currentPointer = currentPointer.next.next
        
        if oddTeamCounter == evenTeamCounter :
            return "Tie"
        elif oddTeamCounter > evenTeamCounter:
            return "Odd"
        else:
            return "Even"


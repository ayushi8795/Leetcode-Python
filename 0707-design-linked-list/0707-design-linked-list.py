class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        count = 0
        
        while curr:
            if count == index:
                return curr.val
            curr = curr.next 
            count+=1
        
        return -1
        

    def addAtHead(self, val: int) -> None:
        NewNode = ListNode(val)
        NewNode.next = self.head
        self.head = NewNode
            
    def addAtTail(self, val: int) -> None:
        
        if not self.head:
            self.head = ListNode(val)
            return
            
        NewNode = ListNode(val)
        curr = self.head
        
        while curr.next:
            curr = curr.next
        curr.next = NewNode
        return
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index == 0:
            self.addAtHead(val)
            return
        
        newNode = ListNode(val)
        count = 0
        curr = self.head
        while curr and count < index-1:
            curr = curr.next
            count +=1
        if not curr:
            return
        newNode.next = curr.next
        curr.next = newNode
            
    
    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        curr = self.head
        count = 0
        
        while curr.next and count < index-1:
            curr = curr.next
            count +=1
        if curr.next:
            curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
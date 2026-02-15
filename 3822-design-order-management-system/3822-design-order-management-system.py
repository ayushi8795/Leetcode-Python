class OrderManagementSystem:

    def __init__(self):
        self.orderManage = {}
        

    def addOrder(self, orderId: int, orderType: str, price: int) -> None:
        self.orderManage[orderId] = [orderType,price]
        

    def modifyOrder(self, orderId: int, newPrice: int) -> None:
        for key,value in self.orderManage.items():
            if key == orderId:
                orderType = value[0]
                self.orderManage[orderId] = [orderType,newPrice]

    def cancelOrder(self, orderId: int) -> None:
        del self.orderManage[orderId]
        

    def getOrdersAtPrice(self, orderType: str, price: int) -> List[int]:
        activeOrderId = []
        for key,value in self.orderManage.items():
            if value[0] == orderType and value[1] == price:
                activeOrderId.append(key)
        return activeOrderId
        


# Your OrderManagementSystem object will be instantiated and called as such:
# obj = OrderManagementSystem()
# obj.addOrder(orderId,orderType,price)
# obj.modifyOrder(orderId,newPrice)
# obj.cancelOrder(orderId)
# param_4 = obj.getOrdersAtPrice(orderType,price)
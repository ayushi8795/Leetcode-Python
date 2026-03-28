class RideSharingSystem:

    def __init__(self):
        self.rider = []
        self.driver = []
        self.activeRider = {}
        

    def addRider(self, riderId: int) -> None:
        self.rider.append(riderId)
        self.activeRider[riderId] = True


    def addDriver(self, driverId: int) -> None:
        
        self.driver.append(driverId)


    def matchDriverWithRider(self) -> List[int]:
        while self.rider and not self.activeRider.get(self.rider[0],False):
            self.rider.pop(0)
        if not self.rider or not self.driver:
            return [-1,-1]
        driverId = self.driver.pop(0)
        riderId = self.rider.pop(0)

        del self.activeRider[riderId]
        return [driverId, riderId]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.activeRider:
            self.activeRider[riderId] = False


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)
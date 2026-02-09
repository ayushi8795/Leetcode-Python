class RecentCounter:

    def __init__(self):
        self.pingValue = []

    def ping(self, t: int) -> int:
        self.pingValue.append(t)
        upperRange = t
        lowerRange = t-3000
        counter = 0
        for i in self.pingValue:
            if lowerRange <= i <=upperRange:
                counter = counter + 1
        return counter

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
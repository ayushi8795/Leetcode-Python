class Logger:

    def __init__(self):
        
        self.nextTime = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.nextTime or timestamp >= self.nextTime[message]:
            self.nextTime[message] = timestamp + 10
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
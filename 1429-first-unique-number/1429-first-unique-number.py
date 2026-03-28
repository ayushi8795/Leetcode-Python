class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums 
        self.numhash = {}
        for nu in self.nums:
            if nu not in self.numhash:
                self.numhash[nu] = 1
            else:
                self.numhash[nu] = self.numhash[nu] +1
        
    def showFirstUnique(self) -> int:

        for i in self.nums:
            if self.numhash[i] == 1:
                return i
        return -1
        

    def add(self, value: int) -> None:
        self.nums.append(value)
        if value in self.numhash:
            self.numhash[value] += 1
        else:
            self.numhash[value] = 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
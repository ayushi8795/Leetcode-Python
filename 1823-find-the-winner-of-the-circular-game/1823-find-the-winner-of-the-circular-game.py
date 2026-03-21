class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends =[]

        for i in range(n):
            friends.append(i+1)
        start_index = 0

        while len(friends) >1:
            removal_index = (start_index + k-1)%len(friends)

            friends.pop(removal_index)

            start_index = removal_index
        return friends[0]
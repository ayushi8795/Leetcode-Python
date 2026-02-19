class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friend = dict(enumerate(friends))
        lis = []

        for nu in order:
             if nu in friend.values():
                lis.append(nu)
        return lis
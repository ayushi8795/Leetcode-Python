class Solution:
    def pivotInteger(self, n: int) -> int:
        totalSum = 0
        pivot = -1
        leftSum = 0

        for i in range(1, n+1):
            totalSum = totalSum + i

        for i in range(1, n+1):
            leftSum = leftSum+i
            # i is added again beacuse if pivot it needs to be counted twice once in left sum and once in right
            rightSum = totalSum-leftSum + i
            if leftSum == rightSum:
                pivot = i
        return pivot

        
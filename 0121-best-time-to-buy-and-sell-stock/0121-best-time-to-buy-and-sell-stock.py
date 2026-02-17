class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = float('inf')
        maxProf = 0

        for i in range(len(prices)):
            if prices[i] < minBuy:
                minBuy = prices[i]
            elif prices[i] - minBuy > maxProf:
                maxProf = prices[i]-minBuy
        return maxProf
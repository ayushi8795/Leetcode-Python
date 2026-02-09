class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # finalPrice = []
        # for i in range(len(prices)):
        #     j = i+1
        #     discountCalculated = False
        #     while j < len(prices):
        #         if prices[j] <= prices[i]:
        #             finalPrice.append(prices[i]-prices[j])
        #             discountCalculated = True
        #             break
        #         else:
        #             j = j+1
        #     if not discountCalculated:
        #         finalPrice.append(prices[i])
        # return finalPrice

        stack = []
        res = prices
        for index, price in enumerate(prices):
            while stack and stack[-1][0] >= price:
                stackprice, stackindex = stack.pop()
                res[stackindex] =  stackprice-price
            stack.append([price,index])
        return res

            
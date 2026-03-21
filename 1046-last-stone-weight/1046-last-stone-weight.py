class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        neg_stones = [-sto for sto in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) >1:
            max1 = -heapq.heappop(neg_stones)
            max2 = -heapq.heappop(neg_stones)

            if max1==max2:
                max1 = max2 = 0
            else:
                heapq.heappush(neg_stones,-abs(max1-max2))

        if len(neg_stones) == 1:
            return -neg_stones[0]
        else:
            return 0

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        giftHeap = [-gift for gift in gifts]
        heapq.heapify(giftHeap)
        
        for _ in range(k):
            max_gift = -heapq.heappop(giftHeap)
            max_gift = max_gift**0.5
            heapq.heappush(giftHeap,-int(max_gift))
        return -sum(giftHeap)

        
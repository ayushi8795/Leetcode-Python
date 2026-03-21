import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = []
        for i,val in enumerate(nums):
            pq.append((val,i))  # Val comes efore coz, heap needs to be created using val and not index
        print(pq)

        heapify(pq)
        print(pq)

        for _ in range(k):
            val,index = heappop(pq)
            nums[index] *= multiplier
            heappush(pq,(nums[index],index))

        return nums
        
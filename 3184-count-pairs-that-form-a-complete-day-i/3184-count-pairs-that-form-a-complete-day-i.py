class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        
        rem_count = defaultdict(int)
        count = 0

        for hr in hours:
            rem = hr%24

            if rem == 0:
                count += rem_count[0]
            else:
                count += rem_count[24-rem]
            rem_count[rem]+=1
        return count
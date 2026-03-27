class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # h cant be less than len(piles), coz If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour

        minSpeed = 1
        maxSpeed = max(piles)  # in one hr she can eat at most max(pile) banana

        

        while minSpeed < maxSpeed :
            midSpeed = (minSpeed+maxSpeed)//2  # check if the middle speed is okay 
            curr_hr = 0

            for ban in piles:
                curr_hr+=math.ceil(ban/midSpeed)    # this will give hrs required to eat all banana with "midSpeed"

            if curr_hr <= h:
                maxSpeed = midSpeed   # if hr s less than h then we can try to find slower speed by setting the new max to midSpeed
            else:
                minSpeed = midSpeed +1  # if gotten speed is more then we get new min speed

        return maxSpeed




 
        
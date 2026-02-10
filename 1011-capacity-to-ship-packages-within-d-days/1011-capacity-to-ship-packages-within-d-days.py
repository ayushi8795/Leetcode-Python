class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lowCap = max(weights)
        # if day == 1
        highCap = sum(weights)

        while lowCap <= highCap:
            midCap = (lowCap+highCap)//2
            currDay = 1
            eachdayweigh = 0

            for w in weights:
                if eachdayweigh+w <= midCap:
                    eachdayweigh+=w
                else:
                    currDay+=1
                    eachdayweigh = w

            if currDay <= days:
                highCap= midCap-1
            else:
                lowCap = midCap+1
        return lowCap


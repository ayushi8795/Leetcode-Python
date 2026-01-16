class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        gainAtPoint0 = 0 # Since altitiude is 0 means biker just started the trip
        n= len(gain)
        highaltitude = [0] # net gain 0 at point 0

        for i in range(n):
            #[-1] because top element has all the calculated value of netgain of previous points
            NetGain = highaltitude[-1] + gain[i]
            highaltitude.append(NetGain)
            
        return max(highaltitude)
            



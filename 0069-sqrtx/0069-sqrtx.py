class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        lower = 2
        upper = x // 2 
        
        while lower <= upper:
            mid = lower+(upper-lower) // 2
            sq = mid * mid
            
            if sq > x:
                upper = mid -1
            elif sq < x:
                lower = mid +1
            else:
                return mid
        return upper
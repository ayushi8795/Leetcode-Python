class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxNo= max(candies)
        arr =[]

        for i in candies:
            if i + extraCandies >= maxNo:
                arr.append(True)
            else:
                arr.append(False)
        return arr
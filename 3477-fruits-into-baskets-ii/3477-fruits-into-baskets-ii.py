class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        for eachf in fruits:
            for b in range(len(baskets)):
                if eachf <= baskets[b]:
                    baskets[b] = 0
                    break
        
        for i in baskets:
            if i !=0:
                count = count+1
        
                
        return count
            
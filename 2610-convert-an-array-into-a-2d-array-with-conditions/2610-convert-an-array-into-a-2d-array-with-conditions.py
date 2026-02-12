class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        hashi = {}
        defaulthashkey = 0

        for nu in nums:
            Placed = False
            if not hashi:
                hashi[defaulthashkey] = [nu]
                Placed = True
            else:
                for key,value in list(hashi.items()):
                    if nu not in value:
                        value.append(nu)
                        Placed = True
                        break
            if not Placed:
                defaulthashkey +=1
                hashi[defaulthashkey] = [nu]

        return [value for key,value in hashi.items()]
                


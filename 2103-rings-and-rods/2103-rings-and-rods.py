class Solution:
    def countPoints(self, rings: str) -> int:
        
        ring_dic = defaultdict(set) 
        count = 0

        for i in range(0,len(rings),2):
            if rings[i+1] not in ring_dic:
                ring_dic[rings[i+1]]  = {rings[i]}
            else:
                ring_dic[rings[i+1]].add(rings[i])

        for key,value in ring_dic.items():
            if len(value) == 3:
                count = count+1
        return count
                  
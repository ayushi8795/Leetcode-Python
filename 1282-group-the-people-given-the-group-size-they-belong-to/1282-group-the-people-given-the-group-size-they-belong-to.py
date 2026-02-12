class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        fre = {}

        for index,value in enumerate(groupSizes):
            if value not in fre:
                fre[value] = [index]
            else:
                fre[value].append(index)


        for key, value in fre.items():
            for i in range(0,len(value),key):
                ans.append(value[i:i+key])
        return ans
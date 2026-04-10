class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_name = dict(zip(heights,names))
        sorted_height = sorted(heights, reverse = True)

        sort_name = []

        for i in sorted_height:
             sort_name.append(height_name[i])
        return sort_name
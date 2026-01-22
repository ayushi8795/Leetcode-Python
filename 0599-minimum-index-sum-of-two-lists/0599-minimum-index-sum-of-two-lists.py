class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lis1 = {}
        lis = []

        for i in list1:
            if i not in lis1 and i in list2:
                lis1[i] = list1.index(i) + list2.index(i)

        dic = sorted(lis1.items(), key=lambda item: item[1])

        flip = defaultdict(list)
        for key, value in dic:
            flip[value].append(key)

        return next(iter(flip.values()))
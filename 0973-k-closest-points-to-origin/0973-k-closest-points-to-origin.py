class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        result = []

        for x,y in points:
            dis = math.sqrt((x-0)**2+(y-0)**2)
            distance.append((dis,[x,y]))
        distance.sort()
        distance = distance[:k]
        return [dis[1] for dis in distance]

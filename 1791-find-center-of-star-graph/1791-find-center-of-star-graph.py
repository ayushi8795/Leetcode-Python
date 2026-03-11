class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        mapdic = {}
        maxi = 0
        keyz = -1
        for edge in edges:
            u = edge[0]
            v = edge[1]
            if u in mapdic:
                mapdic[u].append(v)
            if v in mapdic:
                mapdic[v].append(u)
            if u not in mapdic:
                mapdic[u] = [v]
            if v not in mapdic:
                mapdic[v] = [u]

        for key, value in mapdic.items():
            if maxi < len(value):
                maxi = len(value)
                keyz = key
        return keyz

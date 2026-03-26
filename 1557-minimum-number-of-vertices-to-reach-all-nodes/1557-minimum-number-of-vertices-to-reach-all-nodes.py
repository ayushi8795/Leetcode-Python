class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        visited = set()
        res = []

        for node in edges:
            out_node, in_node = node[0],node[1]

            visited.add(in_node)

        for i in range(n):
            if i not in visited:
                res.append(i)
        return res

        
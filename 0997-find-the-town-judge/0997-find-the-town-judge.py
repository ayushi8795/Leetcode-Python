class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # Trusted by everyone
        indegree = [0]*(n+1)

        #Trust nobody
        outdegree = [0]*(n+1)

        for a,b in trust:
            outdegree[a] +=1
            indegree[b] +=1
        
        for person in range(1,n+1):
            if outdegree[person]==0 and indegree[person] == n-1:
                return person
        return -1



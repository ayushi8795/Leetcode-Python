class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        visited = {}
        result = []
        
        for nu in nums1:
            visited[nu] = 1

        for nu in nums2:
            if nu in visited and visited[nu] == 1:
                result.append(nu)
                visited[nu] = 0
        return result
        
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashi = OrderedDict()

        for i in arr:
            if i not in hashi:
                hashi[i] = 1
            else:
                hashi[i] = hashi[i] + 1

        lis = []

        for key, value in hashi.items():
            if value == 1:
                lis.append(key)
        if len(lis) >= k:
            return lis[k-1]
        else:
             return ""
            
            
        
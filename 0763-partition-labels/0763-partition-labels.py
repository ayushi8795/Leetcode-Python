class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occur_dict = {}
        partition_start = 0
        partition_end =0
        partition_Size = []

        for index, char in enumerate(s):
            last_occur_dict[char] = index
        
        for index, char in enumerate(s):
            partition_end = max(partition_end,last_occur_dict[char])
            if index == partition_end:
                partition_Size.append(index-partition_start+1)
                partition_start = index+1
        return partition_Size
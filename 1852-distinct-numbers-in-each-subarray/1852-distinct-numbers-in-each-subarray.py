class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        len_num = len(nums)
        ans = [0]* (len_num-k+1)
        freq = {}

        for nu in range(k):
            if nums[nu] in freq:
                freq[nums[nu]]+=1
            else:
                freq[nums[nu]] = 1
        ans[0] = len(freq)

        for pos in range(k, len_num):
            # delete left most element
            left = nums[pos-k]
            freq[left] -=1
            if freq[left] ==0:
                del freq[left]
            
            if nums[pos] in freq:
                freq[nums[pos]]+=1
            else:
                freq[nums[pos]] = 1

            ans[pos-k+1] = len(freq)
        return ans


            


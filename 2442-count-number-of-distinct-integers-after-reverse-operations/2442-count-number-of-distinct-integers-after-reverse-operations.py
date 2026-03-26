class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        len_num = len(nums)
        set_num = set(nums)
        
        for n in nums:
            reverse_n =0
            while n!= 0:
                #Extract Last Digit
                dig = n%10
                # * by 10 so that it comes 1st
                reverse_n = reverse_n*10+dig

                n = n // 10

            set_num.add(reverse_n)
        return len(set_num)

        
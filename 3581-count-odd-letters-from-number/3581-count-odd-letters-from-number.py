class Solution:
    def countOddLetters(self, n: int) -> int:
        num_to_str = {
            1 : 'one',
            2 : 'two',
            3 : 'three',
            4 : 'four',
            5 : 'five',
            6 : 'six',
            7 : 'seven',
            8 : 'eight',
            9 : 'nine',
            0 : 'zero' 
        }

        s = ''
        count = 0
        freq = {}

        for i in str(n):
            s  = s + num_to_str[int(i)]
        
        for j in s:
            if j not in freq:
                freq[j] = 1
            else:
                freq[j] = freq[j]+1
        for key,value in freq.items():
            if value%2 != 0 :
                count= count+1
        return count
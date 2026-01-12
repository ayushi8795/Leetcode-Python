class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        index = 0
        result = []

        #### This solution is also correct just it uses stack.
        # while index < len(word):
        #     # Add to stack
        #     stack.append(word[index])

        #     if word[index] == ch:
        #         # pop till stack is empty
        #         while stack:
        #             result.append(stack.pop())
        #         # index updated so that next element can be added and same index from the word is taken into consideration
        #         index = index+1
        #         # copy rest of the original word
        #         while index < len(word):
        #             result.append(word[index])
        #             index = index+1
        #         # join it 
        #         return ''.join(result)
        #     # update the index if no ch found till last
        #     index = index+1
        # return word

        x= -1
        for i in range(len(word)):
            if word[i] == ch:
                x = i
                break
        if x != -1:
            l=0
            r=x
            word = list(word) 
            while l<r:
                word[l],word[r]=word[r],word[l]
                l=l+1
                r = r-1
            return "".join(word)
        return word
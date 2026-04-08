class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        word1_combine = ''
        word2_combine = ''

        for i in word1:
            word1_combine = word1_combine + i

        for j in word2:
            word2_combine = word2_combine +j
            
        return word2_combine == word1_combine

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        default = -1

        pointer = 0
        sentence = sentence.split(" ")
        print(sentence)

        while pointer < len(sentence):

            if searchWord in sentence[pointer][:len(searchWord)]:
                return pointer +1
            pointer +=1
        return default
            
        
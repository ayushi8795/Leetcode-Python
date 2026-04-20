class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        alph_morse = dict(zip(alph,morse))
        
        trans = set()

        for wor in words:
            s = ''
            for char in wor:
                s = s + alph_morse[char]
            trans.add(s)
        return len(trans)


       
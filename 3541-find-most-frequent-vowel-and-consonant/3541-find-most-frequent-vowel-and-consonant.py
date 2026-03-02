class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {}
        consonants = {}
        maxConsonants = 0
        maxVowels =0
        for i in s:
            if i in {'a','e','i','o','u'}:
                if i not in vowels:
                    vowels[i] = 1
                else:
                    vowels[i] +=1
            else:
                if i not in consonants:
                    consonants[i] = 1
                else:
                    consonants[i]+=1
        if vowels:
            maxVowels = max(vowels.values())
        if consonants:
            maxConsonants = max(consonants.values())

        return maxConsonants+maxVowels
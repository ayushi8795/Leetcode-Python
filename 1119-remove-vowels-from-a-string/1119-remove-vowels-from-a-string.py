class Solution:
    def removeVowels(self, s: str) -> str:
        st = ['a','e','i','o','u']
        final =''

        for char in s:
            if char not in st:
                final = final+char
        return final
        
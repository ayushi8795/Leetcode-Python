class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashi = set()

        for i in sentence:
            hashi.add(i)
        
        return len(hashi)==26
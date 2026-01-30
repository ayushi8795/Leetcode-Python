class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        l = 0
        h = len(letters)-1

        while l <= h:
            mid = (l+h)//2

            if ord(letters[mid]) <= ord(target):
                l = mid +1
            else:
                h = mid -1
        

        if l == len(letters):
            return letters[0]
        else:
            return letters[l]

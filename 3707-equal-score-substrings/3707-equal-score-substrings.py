class Solution:
    def scoreBalance(self, s: str) -> bool:
        
        totalSum = 0
        leftSum = 0
        for i in range(len(s)):
            totalSum = totalSum + ord(s[i])-ord("a")+1

        for i in range(len(s)-1):
            leftSum = leftSum +  (ord(s[i])-ord("a")+1)
            print(leftSum)
            rightSum = totalSum - leftSum
            print(rightSum)
            if leftSum == rightSum:
                return True
        return False


        
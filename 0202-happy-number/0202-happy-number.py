class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()

        while n not in visited:
            visited.add(n)
            print(visited)
            n = self.sumOfSqure(n)

            if n == 1:
                return True
        return False

    def sumOfSqure(self,n):
        output = 0
        # while n mean n!=0
        while n:
            digit = n%10
            print("digit",digit)
            digit = digit**2
            output +=digit
            n = n//10 # this is used to get the next number after 9 i.e. 1
            print("Self.sumofSqure", n)
        return output


            
        
        
        
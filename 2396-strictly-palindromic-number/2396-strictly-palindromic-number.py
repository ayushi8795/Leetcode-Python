class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # calcuate the range of for bases
        baseRange = [2,n-2+1]

        for i in range(baseRange[0],baseRange[1]):
            lis = self.baseVal(n,i,[])
            if not self.pali(lis):
                return False
    
    # function to form base conversion
    def baseVal(self,n,base,lis):
        while n > 0:
            # insert in reverse because of Math
            lis.insert(0,int(n%base))
            #calls it self until the quotient becomes 0
            return self.baseVal(int(n/base) , base, lis)

            # returns the converted value back to for loop 
        return lis
    
    #checks for palindrom, if single false means no additonal calculation needed
    def pali(self,lis):
        start = 0
        end = len(lis)-1

        while start < end:
            if lis[start] == lis[end]:
                start = start + 1
                end = end-1
            else:
                return False
        return True
    
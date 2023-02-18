class Solution:

    def breakInteger(self,n,totalSoFar=0):
        if n<=9:
            return n**2+totalSoFar
        
        return self.breakInteger(int(n/10),totalSoFar+(n%10)**2)

    def isHappy(self, n: int) -> bool: 

        seen = set()

        while(n!=1 and n not in seen):
            seen.add(n)
            n = self.breakInteger(n)
            
        return n==1
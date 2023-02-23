class Solution:
    def addBinary(self, a: str, b: str) -> str:

        c = ""
        carry=0

        i,j= len(a)-1,len(b)-1
        while(i>=0 or j>=0):
            elem1=int(a[i]) if i>=0 else 0
            elem2=int(b[j]) if j>=0 else 0

            total = elem1+elem2+carry
            c = str(total%2) + c
            carry = total//2
            i-=1
            j-=1

        if carry:
            c = "1" + c

        return c
            


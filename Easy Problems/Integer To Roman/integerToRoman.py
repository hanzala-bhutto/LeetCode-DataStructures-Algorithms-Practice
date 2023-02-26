class Solution:

    # roman goes from largest to smallest
    # that is why storing in reverse order
    # number is number and symbol is roman stored with that number
    def intToRoman(self, num: int) -> str:
        hashList=[[1000,"M"],[900, "CM"],[500,"D"],[400,"CD"],[100,"C"],
                [90,"XC"],[50,"L"],[40,"XL"],[10,"X"],[9,"IX"],[5,"V"],[4,"IV"],
                [1,"I"]]
        
        res = ""
        for number,symbol in hashList:
            # go from largest to smallest
            if num//number:
                countTimes=num//number
                res+=(symbol*countTimes) # roman*countOfRoman 
                num%=number

        return res
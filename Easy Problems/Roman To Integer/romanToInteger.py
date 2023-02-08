
def romanToInt(s:str) -> int:
    
    h = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    
    i=0
    integer = 0
    while(i<len(s)):
        if(i+1<len(s)):
            if(s[i]=='I' and (s[i+1]=='V' or s[i+1]=='X')):
                integer+=h[s[i+1]]-h[s[i]]
                i+=2
            elif(s[i]=='X' and (s[i+1]=='L' or s[i+1]=='C')):
                integer+=h[s[i+1]]-h[s[i]]
                i+=2
            elif(s[i]=='C' and (s[i+1]=='D' or s[i+1]=='M')):
                integer+=h[s[i+1]]-h[s[i]]
                i+=2
            else:
                integer+=h[s[i]]
                i+=1
        else:
            integer+=h[s[i]]
            i+=1
        
    return integer

# Test case 1
s = "III"

# # Test case 2
s = "LVIII"

# # Test case 3
s = "MCMXCIV"

result = romanToInt(s)
print(result)
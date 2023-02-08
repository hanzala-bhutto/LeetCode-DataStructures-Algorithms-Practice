def romanToInt(s: str) -> int:
    h = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    
    integer = 0
    for i in range(len(s)):
        if i==len(s)-1 or h[s[i]]>=h[s[i+1]]:
            integer+=h[s[i]]
        else:
            integer-=h[s[i]]

    return integer

# Test case 1
s = "III"

# # Test case 2
s = "LVIII"

# # Test case 3
s = "MCMXCIV"

result = romanToInt(s)
print(result)
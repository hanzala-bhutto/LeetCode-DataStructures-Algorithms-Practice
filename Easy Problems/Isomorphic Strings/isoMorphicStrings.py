class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hashMap = {}
        hashSet = set()

        for i in range(len(s)):
            if s[i] in hashMap:
                if hashMap[s[i]] != t[i]:
                    return False
            else:
                if t[i] in hashSet:
                    return False
                hashMap[s[i]]=t[i]
                hashSet.add(t[i])
        
        return True

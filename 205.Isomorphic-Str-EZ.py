class Solution: # O(N) Time & O(1) Space. 
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap = {} 
        hashSet = set() 

        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            if (sChar not in hashMap):
                if (tChar in hashSet):
                    return False 
                hashMap[sChar] = tChar
                hashSet.add(tChar)
            else:
                if (tChar != hashMap[sChar]):
                    return False 
        return True 
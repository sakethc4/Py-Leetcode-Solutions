class Solution: # O(N) Time & O(1) Space. 
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer1, pointer2 = 0, 0
        while pointer1 < len(s) and pointer2 < len(t):
            if s[pointer1] == t[pointer2]:
                pointer1 += 1 
            pointer2+= 1
        return pointer1 == len(s)
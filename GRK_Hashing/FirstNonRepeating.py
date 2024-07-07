class Solution: # O(N) Time & O(N) Space. 
    def firstUniqChar(self, s: str) -> int:
        hashMap = {} 
        for char in s: 
            hashMap[char] = 1 + hashMap.get(char, 0)
        for index in range(len(s)):
            if hashMap[s[index]] == 1:
                return index 
        return -1

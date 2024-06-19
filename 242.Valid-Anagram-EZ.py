from collections import Counter
class Solution: # O(N) Time & O(N) Space. This solution just looks cleaner. 
    # We want to check if each word (s,t) has identical letters 
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
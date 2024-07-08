from collections import defaultdict

class Solution: # O(N) Time & O(1) Space. 
    def maxNumberOfBalloons(self, text: str) -> int:
        minCount = float('inf')
        hashMap = defaultdict(int)
        for char in text:
            hashMap[char] += 1
        minCount = min(minCount, hashMap['b'])
        minCount = min(minCount, hashMap['a'])
        minCount = min(minCount, hashMap['l'] // 2)
        minCount = min(minCount, hashMap['o'] // 2)
        minCount = min(minCount, hashMap['n'])
        return minCount
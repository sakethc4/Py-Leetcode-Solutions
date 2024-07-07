from collections import defaultdict

class Solution: # O(N) Time & O(N) Space. 
    def largestUniqueNumber(self, A: List[int]) -> int:
        largest = -1 
        hashMap = {} 
        for num in A:
            hashMap[num] = 1 + hashMap.get(num, 0)
        for key, value in hashMap.items():
            if value == 1:
                largest = max(largest, key)
        
        return largest
            
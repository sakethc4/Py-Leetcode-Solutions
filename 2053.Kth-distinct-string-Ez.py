class Solution: # O(N) Time & O(N) Space.
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr) # key: "a" => value: "1"
        for element in arr: 
            if counter[element] == 1:
                k -= 1 
            if k == 0: 
                return element 
        
        return ""
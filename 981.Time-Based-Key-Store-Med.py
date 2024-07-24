class TimeMap:
# O(LogN) Time & O(N) Space. 
    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore: 
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result, values = "", self.keyStore.get(key, [])
        start, end = 0, len(values) - 1
        while start <= end: 
            middle = start + (end - start) // 2 
            if timestamp >= values[middle][1]:
                result = values[middle][0]
                start = middle + 1
            else: 
                end = middle - 1 

        return result 



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
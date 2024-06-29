class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val 
        self.previous = self.next = None 


class LRUCache: # O(N) Time & O(N) Space. 
    def __init__(self, capacity: int):
        self.capacity = capacity 
        # Initialize a hashMap. 
        self.cache = {} 
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.previous = self.right, self.left

    # remove node from list
    def remove(self, node):
        previous, next = node.previous, node.next 
        previous.next, next.previous = next, previous 
    
    # insert node at right
    def insert(self, node):
        previous, next = self.right.previous, self.right 
        previous.next = next.previous = node 
        node.previous, node.next = previous, next
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.remove(self.cache[key])
        # Adding to hashMap. 
        self.cache[key] = Node(key, value)
        # Handle LinkedList. 
        self.insert(self.cache[key])
        # Handle reaching capacity. 
        if len(self.cache) > self.capacity: 
            least = self.left.next
            # Remove the Node. 
            self.remove(least)
            # Delete from the HashMap. 
            del self.cache[least.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]': # O(N) Time & O(N) Space. 
        # Make sure to add a None : None key and value in case a random points to a null value. 
        originalToCopy = {None : None} 
        # First let's get all the nodes and add them to our hashMap. 
        current = head 
        while current is not None: 
            copy = Node(current.val)
            originalToCopy[current] = copy 
            current = current.next 
        # Now add pointers. 
        current = head 
        while current is not None: 
            copy = originalToCopy[current]
            copy.next = originalToCopy[current.next]
            copy.random = originalToCopy[current.random]
            current = current.next
        # Return now that we have our deep copy. 
        return originalToCopy[head] 
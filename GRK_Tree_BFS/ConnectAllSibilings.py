from collections import deque

#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = self.right = self.next = None

class Solution: # O(N) Time & O(N) Space.
    def connect(self, root):
        if root is None:
            return root
        queue = deque() 
        queue.append(root)
        while queue:  
            previous = None 
            levelSize = len(queue)
            for _ in range(levelSize):
                currNode = queue.popleft() 
                if previous: 
                    previous.next = currNode
                previous = currNode
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
        return root


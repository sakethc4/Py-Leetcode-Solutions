from collections import deque


#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution: # O(N) Time & O(N) Space. 
  def findDepth(self, root):
    result = float('inf')
    if root is None:
      return result 
    queue = deque()
    queue.append(root)
    depth = 0 
    while queue:
      levelSize = len(queue)
      for _ in range(levelSize):
        currNode = queue.popleft() 
        if currNode.left:
          queue.append(currNode.left)
        if currNode.right:
          queue.append(currNode.right)
        if currNode.left is None and currNode.right is None:
          result = min(depth + 1, result)
      depth += 1    
    return result  


from collections import deque


#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution: # O(N) Time & O(N) Space. 
  def traverse(self, root):
    result = [] 
    # Validate root. 
    if root is None:
      return result 
    queue = deque() 
    queue.append(root)
    while queue: 
      levels = len(queue)
      currLevel = [] 
      for _ in range(levels):
        currentNode = queue.popleft() 
        currLevel.append(currentNode.val)
        if currentNode.left:
          queue.append(currentNode.left)
        if currentNode.right:
          queue.append(currentNode.right)
      result.append(currLevel)
    return result 
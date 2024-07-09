from collections import deque

#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution: # O(N) Time & O(N) Space. 
  def traverse(self, root):
    result = deque()
    if root is None: 
      return result 
    queue = deque() 
    queue.append(root)
    while queue: 
      currLvl = []
      levels = len(queue)
      for _ in range(levels):
        currNode = queue.popleft()
        currLvl.append(currNode.val)
        if currNode.left:
          queue.append(currNode.left)
        if currNode.right:
          queue.append(currNode.right)
      result.appendleft(currLvl)
    
    result = [list(sublist) for sublist in result]
    return result 
from collections import deque


#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution: # O(N) Time & O(N) Space. 
  def findLevelAverages(self, root):
    result = []
    if root is None: 
      return result
    queue = deque() 
    queue.append(root)
    while queue:
      levelAvg = 0  
      levelSize = len(queue)
      for _ in range(levelSize):
        currNode = queue.popleft()
        levelAvg += currNode.val
        if currNode.left:
          queue.append(currNode.left)
        if currNode.right:
          queue.append(currNode.right)
      result.append(levelAvg / levelSize) 
    return result

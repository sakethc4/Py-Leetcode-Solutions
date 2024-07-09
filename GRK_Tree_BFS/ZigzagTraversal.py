from collections import deque

#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution: # O(N) Time & O(N) Space. 
  def traverse(self, root):
    leftToRight = True
    result = []
    queue = deque()
    if root is None:
      return result 
    queue.append(root)
    while queue:
      currLvl = deque()
      levelSize = len(queue)
      for _ in range(levelSize):
        currNode = queue.popleft()
        if leftToRight:
          currLvl.append(currNode.val)
        else: 
          currLvl.appendleft(currNode.val)

        if currNode.left:
          queue.append(currNode.left)
        if currNode.right:
          queue.append(currNode.right)

      result.append(list(currLvl))
      leftToRight = not leftToRight
    return result  
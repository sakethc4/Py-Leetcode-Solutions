from collections import deque

#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution: # O(N) Time & O(N) Space. 
  def traverse(self, root):
    result = []
    if root is None:
      return root 
    queue = deque()
    queue.append(root)
    while queue: 
      rightView = deque() 
      levelSize = len(queue)
      for _ in range(levelSize):
        currNode = queue.popleft() 
        rightView.appendleft(currNode.val)
        if currNode.left:
          queue.append(currNode.left)
        if currNode.right:
          queue.append(currNode.right)
      result.append(rightView[0])


    return result

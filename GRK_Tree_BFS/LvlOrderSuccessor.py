from collections import deque


#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None


class Solution: # O(N) Time & O(N) Space. 
  def findSuccessor(self, root, key):
    queue = deque()
    queue.append(root)
    while queue:
      currNode = queue.popleft() 
      if currNode.left:
        queue.append(currNode.left)
      if currNode.right:
        queue.append(currNode.right)

      if currNode.val == key:
        break

    return queue[0] if queue else None   



    return root

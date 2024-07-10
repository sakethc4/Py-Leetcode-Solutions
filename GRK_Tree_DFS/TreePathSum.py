#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution: # O(N) Time & O(N) Space. 
  def hasPath(self, root, sum):
    if root is None: 
      return False 
    # Case 1. Found sum and we are at a leaf node. 
    if root.val == sum and root.left is None and root.right is None:
      return True 
    return self.hasPath(root.left, sum - root.val) or self.hasPath(root.right, sum - root.val)

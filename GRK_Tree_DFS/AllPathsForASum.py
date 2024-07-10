#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution: # O(NLogN) Time & O(NLogN) Space. 
  def findPaths(self, root, required_sum):
    allPaths = []
    self.findPathsAux(root, required_sum, [], allPaths)
    return allPaths 
    
  def findPathsAux(self, root, required_sum, currentPath, allPaths):
    if root is None: 
      return
    # What is current path we are looking at. 
    currentPath.append(root.val)
    # Case where we find sum and we are at a leaf node. 
    if root.val == required_sum and root.left is None and root.right is None:
      allPaths.append(list(currentPath))
    else:
      # Traverse left side. 
      self.findPathsAux(root.left, required_sum - root.val, currentPath, allPaths)
      # Traverse the right side. 
      self.findPathsAux(root.right, required_sum - root.val, currentPath, allPaths)

    del currentPath[-1]
    
    
    return allPaths
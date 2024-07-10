#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution: # O(N) Time & O(N) Space. 
  def findSumOfPathNumbers(self, root): 
    return self.findSumOfPathNumbersAux(root, 0)
  
  def findSumOfPathNumbersAux(self, currNode, pathSum):
    if currNode is None: 
      return 0 
    
    # Find the pathSum. 
    pathSum = pathSum * 10 + currNode.val 
    # Case where we find a leaf node. 
    if currNode.left is None and currNode.right is None:
      return pathSum 
    
    # Need to traverse the other two children 
    return self.findSumOfPathNumbersAux(currNode.left, pathSum) + self.findSumOfPathNumbersAux(currNode.right, pathSum)
    
    
#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution: # O(N) Time & O(N) Space.
  def findPath(self, root, sequence):
    return self.findPathAux(root, [], sequence)
  
  def findPathAux(self, currNode, currPath, sequence):
    if currNode is None:
      return False
    currPath.append(currNode.val)
    # Case where we found our sequence. 
    if currPath == sequence and currNode.left is None and currNode.right is None:
      return True

    checkLeft = self.findPathAux(currNode.left, currPath, sequence)
    checkRight = self.findPathAux(currNode.right, currPath, sequence)
    del currPath[-1]

    return checkLeft | checkRight 
    

    

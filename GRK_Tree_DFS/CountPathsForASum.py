#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution: # O(N)^2 Time & O(N) Space.
  def countPaths(self, root, S):
    return self.countPathsAux(root, S, [])
  
  def countPathsAux(self, currNode, S, currPath):
    if currNode is None:
      return 0
    currPath.append(currNode.val)
    pathSum, totalSum = 0, 0
    for index in range(len(currPath) - 1, -1, -1):
      pathSum += currPath[index]
      if pathSum == S:
        totalSum += 1 
    # Now traverse left and right. 
    totalSum += self.countPathsAux(currNode.left, S, currPath)
    totalSum += self.countPathsAux(currNode.right, S, currPath)
    del currPath[-1]

    return totalSum
    
  


     

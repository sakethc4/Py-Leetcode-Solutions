import math

#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right


class Solution: # O(N) Time & O(N) Space. 
  def findMaximumPathSum(self, root):
    self.globalMaxPathSum = -math.inf
    self.findMaxPathSumAux(root)
    return self.globalMaxPathSum

  def findMaxPathSumAux(self, currNode):
    if currNode is None: 
      return 0
    
    maxPathLeft = self.findMaxPathSumAux(currNode.left)
    maxPathRight = self.findMaxPathSumAux(currNode.right)

    maxPathLeft = max(maxPathLeft, 0)
    maxPathRight = max(maxPathRight, 0)
    # Now we need to update our local path sum. 
    localMaxPathSum = maxPathLeft + maxPathRight + currNode.val
    # Update our global. 
    self.globalMaxPathSum = max(localMaxPathSum, self.globalMaxPathSum)

    # Return. 
    return max(maxPathLeft, maxPathRight) + currNode.val 
    
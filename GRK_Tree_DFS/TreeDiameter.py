#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right


class Solution: # O(N) TIme & O(N) Space. 
  def __init__(self):
    self.treeDiameter = 0

  def findDiameter(self, root):
    self.findHeight(root)
    return self.treeDiameter
    
  def findHeight(self, currNode):
    if currNode is None: 
      return 0

    leftTreeHeight = self.findHeight(currNode.left)
    rightTreeHeight = self.findHeight(currNode.right)

    if leftTreeHeight != 0 and rightTreeHeight != 0:
      diameter = leftTreeHeight + rightTreeHeight + 1 
      self.treeDiameter = max(self.treeDiameter, diameter)

    return max(leftTreeHeight, rightTreeHeight) + 1 

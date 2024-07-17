# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        root, forest = self.dfs(root, set(to_delete))
        return forest+[root] if root else forest 

    def dfs(self, currNode, setToDelete):
        if currNode is None:
            return None, [] 
        currNode.left, forestL = self.dfs(currNode.left, setToDelete)
        currNode.right, forestR = self.dfs(currNode.right, setToDelete)
        forest = forestL + forestR
        if currNode.val in setToDelete:
            if currNode.left:
                forest.append(currNode.left)
            if currNode.right: 
                forest.append(currNode.right)
            return None, forest 
        return currNode, forest 
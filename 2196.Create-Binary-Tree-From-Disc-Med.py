# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(N) Time & O(N) Space. 
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hashMap = {} 
        parents = set() 
        # Creating the nodes. 
        for param in descriptions: 
            if param[0] not in hashMap: 
                hashMap[param[0]] = TreeNode(param[0])
            if param[1] not in hashMap:
                hashMap[param[1]] = TreeNode(param[1])
            parents.add(param[1])
        # Connect the Nodes.
        root = None 
        for param in descriptions:
            if param[2] == 1: 
                hashMap[param[0]].left = hashMap[param[1]]
            else: 
                hashMap[param[0]].right = hashMap[param[1]]
            # Handle setting root. 
            if param[0] not in parents: 
                root = hashMap[param[0]]
        return root 
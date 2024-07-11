# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(N) Time & O(N) Space. 
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [] 
        if root is None: 
            return result 
        queue = deque() 
        queue.append(root)
        while queue: 
            subLvl = [] 
            lvlSize = len(queue)
            for _ in range(lvlSize):
                currNode = queue.popleft() 
                subLvl.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            result.append(subLvl)
        return result 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: # O(N) Time & O(1) Space. 
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers. 
        slow, fast = head, head 
        # Iterate through input LL. 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
            if fast == slow: 
                return True 
        return False       


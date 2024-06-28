# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # O(N) Time & O(1) Space. 
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head 
        # Move right by n. 
        while n > 0: 
            right = right.next 
            n -= 1 
        # Move left pointer right before element we need to delete. 
        while right is not None: 
            left = left.next 
            right = right.next 
        # Now we have all necessary info we can perform the deletion. 
        left.next = left.next.next
        return dummy.next  

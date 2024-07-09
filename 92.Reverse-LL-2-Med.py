# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # O(N) Time & O(1) Space. 
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: 
            return head 
        current, previous = head, None 
        # Find Left Node. 
        index = 0 
        while current and index < left - 1:
            previous = current 
            current = current.next 
            index += 1 
        # Track the lastNodeOfPrev
        lastNodeOfPrev = previous 
        lastNodeOfSubList = current 
        # Now we can reversal. 
        nxt = None 
        index = 0 
        while current and index < right - left + 1:
            nxt = current.next 
            current.next = previous
            previous = current 
            current = nxt 
            index += 1 
        # Post reversal we need to connect our LL back together. 
        if lastNodeOfPrev is not None: 
            lastNodeOfPrev.next = previous 
        else:
            head = previous 
        # Connect ending portion. 
        lastNodeOfSubList.next = current 
        return head  

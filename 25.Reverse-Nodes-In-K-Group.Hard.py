# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # O(N) Time & O(1) Space. 
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lastNodeOfPrev = dummy 
        # Iteratye through our input List. 
        while True: 
            initialStartingNode = lastNodeOfPrev.next 
            # Handle subList. 
            subList = self.getSubList(lastNodeOfPrev, k)
            if subList is None:
                break 
            firstNodeOfNext = subList.next 
            # Now let's handle reversal. 
            current, previous = lastNodeOfPrev.next, None
            while current != firstNodeOfNext: 
                nxt = current.next 
                current.next = previous 
                previous = current 
                current = nxt
            # Let's handle connecting sublists. 
            # switch dummy.next pointer.
            lastNodeOfPrev.next = subList
            # Switch initialStarting. 
            initialStartingNode.next = firstNodeOfNext
            # Switch lastNodeOfnext. 
            lastNodeOfPrev = initialStartingNode 
        return dummy.next   

    
    # Helper method to find sublists. 
    def getSubList(self, current, k):
        while current and k > 0: 
            current = current.next 
            k -= 1
        return current 

         




         
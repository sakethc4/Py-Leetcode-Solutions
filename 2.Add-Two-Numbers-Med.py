# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # O(N) Time & O(N) Space. 
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # We need to create new LL for our output. 
        # Iterate through both of these and add the two values. 
        # sum % 10 = 0 
        # store sum / 10 and add it to next sum.
        dummy = ListNode() 
        current = dummy 
        remainder = 0 
        while l1 or l2 or remainder:
            value1 = l1.val if l1 else 0  
            value2 = l2.val if l2 else 0 
            # Find new value. 
            newValue = value1 + value2 + remainder 
            remainder = newValue // 10
            newValue = newValue % 10
            current.next = ListNode(newValue)
            # We need to move the l1, l2, and our new List pointers.
            current = current.next  
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None

        return dummy.next 
             

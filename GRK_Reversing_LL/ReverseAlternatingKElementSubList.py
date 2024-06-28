
#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution: # O(N) Time & O(1) Space. 
  def reverse(self, head, k):
    # Validate our input. 
    if head is None or k <= 1: 
      return head 
    # Iterate through input LL.
    current, previous = head, None 
    while current is not None: 
      lastNodeOfPreviousSubList = previous 
      lastNodeofSubList = current
      # Let's now handle reversal. 
      nxt = None 
      index = 0 
      while index < k and current is not None: 
        nxt = current.next 
        current.next = previous 
        previous = current
        current = nxt
        index += 1 
      # Now connect this sublist. 
      if lastNodeOfPreviousSubList is not None:
        lastNodeOfPreviousSubList.next = previous 
      else: 
        head = previous
      # Now handle connecting with next part. 
      lastNodeofSubList.next = current 
      # Now skip values. 
      index = 0 
      while index < k and current is not None:
        previous = current 
        current = current.next
        index += 1 
    return head      


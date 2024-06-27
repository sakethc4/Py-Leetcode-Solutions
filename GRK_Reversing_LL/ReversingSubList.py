#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution: # O(N) Time & O(1) Space. 
  def reverse(self, head, p, q):
    # What do we need to know to do this. 
    # Where does p start. p - 1. 
    # Nodes in p-q. q - p + 1. 
    # Stuff before p. p - 1.
    # Stuff after q. Current Node after we complete reversal. 
    # Account for 1 Node list. 
    if p == q: 
      return head 
    current, previous = head, None 
    index = 0 
    while current is not None and index < p - 1: 
      previous = current 
      current = current.next
      index += 1
    # Track end of first part of LL before p. 
    lastNodeFirstPart = previous 
    # Track where p-q ends post reversal. 
    lastNodeSubList = current 
    # Now reversing p-q. 
    nxt = None 
    index = 0 
    while current is not None and index < q - p + 1: 
      nxt = current.next 
      current.next = previous 
      previous = current
      current = nxt 
      index += 1
    # We need to go through and connect our LL back together. 
    # First part. 
    if lastNodeFirstPart is not None: 
      lastNodeFirstPart.next = previous 
    else: 
      head = previous   
    # Second part. 
    lastNodeSubList.next = current 
    return head  
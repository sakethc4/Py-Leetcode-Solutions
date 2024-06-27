
#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution: # O(N) Time & O(1) Space. 
  def reverse(self, head, k):
    # Need to determine how many nodes to look at during one reversal. 
    # How many to reverse (in single sub-list). While index < k. (Using 0 indexing).
    # Validated the input. 
    if head is None or k <= 0: 
      return head
    current, previous = head, None
    # Iterate through the input. 
    while True:
      lastNodeOfPrevList = previous
      lastNodeOfSubList = current  
      nxt = None
      index = 0  
      while current is not None and index < k: 
        nxt = current.next 
        current.next = previous
        previous = current 
        current = nxt 
        index += 1
      # Join it with the other parts of the LinkedList. 
      if lastNodeOfPrevList is not None: 
        lastNodeOfPrevList.next = previous
      else: 
        head = previous
      # Now we need to move our lastNodeOfSubList pointer. 
      lastNodeOfSubList.next = current    
      if current is None:
        break  
      previous = lastNodeOfSubList
    return head    


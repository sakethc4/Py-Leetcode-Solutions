#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next


class Solution:
    def reverse(self, head):
        prev, curr, nxt = None, head, None
        while curr is not None:
            nxt = curr.next  
            curr.next = prev 
            prev = curr
            curr = nxt 
        return prev

    # 1 -> 2 -> 3. 

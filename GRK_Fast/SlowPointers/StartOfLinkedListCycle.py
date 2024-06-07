class Solution:
    def findCycleStart(self, head): 
        # Given the head of a LL we want to find where the cycle starts. 
        # Sample input: 1 => 2=> 3 => 4 => 5 => 6=> 3 (cycle starts at 3)
        # Tracing input                 
        # Sol. We want a fast and slow pointer and we need to determine where the 
        # cycle starts the first sol that comes to mind is that we figure out where
        # the cycle starts if we figure out where the two pointers meet one another. 
        # They should meet where the cycle starts, so we need to determine the length of 
        # cycle and move the fast pointer by the length, while incrementing the slow one by 1. 
        # ----
        # Initializing the two pointers 
        slow, fast = head, head
        # Variable to keep track of the length 
        cycleLength = 0
        while(fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                cycleLength = self.calculate
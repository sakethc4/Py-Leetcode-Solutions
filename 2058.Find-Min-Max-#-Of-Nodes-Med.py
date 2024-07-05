# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # O(N) Time & O(1) Space. 
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = [-1, -1]
        distance = -1 
        current, previous = head.next, head
        while current.next:
            next = current.next
            if current.val > previous.val and current.val > next.val or current.val < previous.val and current.val < next.val:
                if distance == -1:
                    distance = 0
                else:
                    result[0] = distance if result[0] == -1 else min(result[0], distance)
                    result[1] += distance + (1 if result[1] == -1 else 0)
                    distance = 0
            previous = current
            current = current.next 
            if distance != -1:
                distance += 1
        return result
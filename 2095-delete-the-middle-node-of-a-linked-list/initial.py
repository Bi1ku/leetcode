# Definition for singly-linked list.
import math

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val, self.next = val, next
    
    @staticmethod
    def length(head: ListNode) -> int:
        count = 1

        while head.next != None:
            count += 1
            head = head.next

        return count

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        target = ListNode.length(head) // 2
        print(target, ListNode.length(head))

        # If target is at the head
        if target == 0: return None

        # If target is at the end
        if target == 1 and ListNode.length(head) == 2:
            head.next = None
            return head
        
        # If target is somewhere between
        curr, prev = head.next, head
        while target != 1:
            prev = curr
            curr = curr.next
            target -= 1
        
        prev.next = curr.next
        return head

        # Runtime: O(n)
        # Spacetime: O(1)
        # Can also use two pointers (turtle and hare algo) here

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val, self.next = val, next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev

    # Runtime: O(n)
    # Spacetime: O(1)

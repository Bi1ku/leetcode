# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val, self.next = val, next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next): return head # edge case: 0 or 1 elements in the linked list

        odd_head = ListNode(head.val) # need to start from scratch, otherwise loops would be messed up
        even_head = ListNode(head.next.val)

        # populate the odd linked list
        curr, odd_curr = head, odd_head
        while curr and curr.next and curr.next.next:
            odd_curr.next = ListNode(curr.next.next.val)
            odd_curr = odd_curr.next
            curr = curr.next.next
        
        # populate the even linked list
        curr, even_curr = head.next, even_head
        while curr and curr.next and curr.next.next:
            even_curr.next = ListNode(curr.next.next.val)
            even_curr = even_curr.next
            curr = curr.next.next
        
        odd_curr.next = even_head
        return odd_head
        
        # Runtime: O(n)
        # Spacetime: O(n)
        

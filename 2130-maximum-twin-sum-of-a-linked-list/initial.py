class ListNode:
    def __init__(self, val = 0, next = None):
        self.val, self.next = val, next

    @staticmethod
    def length(head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        sums = {}
        curr, curr_index = head, 0
        n = ListNode.length(head)

        while curr:
            twin = n - 1 - curr_index
            if twin in sums:
                sums[twin] += curr.val
            else:
                sums[curr_index] = curr.val
            curr = curr.next
            curr_index += 1
        
        return max(sums.values())

        # Runtime: O(n + n + n / 2) => O(2.5n) => O(n)
        # Spacetime: O(n / 2) => O(n)

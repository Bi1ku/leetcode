class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow: return True

        return False

l1 = ListNode(1)

sol = Solution()
print(sol.hasCycle(l1))

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        hashset = set()

        while head != None:
            if head in hashset: return True

            hashset.add(head)
            head = head.next

l1 = ListNode(3)
l1.next = ListNode(2)
l1.next.next = ListNode(0)
l1.next.next.next = ListNode(-4)
l1.next.next.next.next = l1.next

sol = Solution()
print(sol.hasCycle(l1))

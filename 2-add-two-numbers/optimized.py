from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        carry, head = 0, ListNode()
        tmp = head

        while (l1 != None or l2 != None):
            sum = carry
            if l1 != None: sum += l1.val
            if l2 != None: sum += l2.val

            carry = sum // 10
            tmp.val = int(sum % 10)

            if (l1 != None and l1.next != None) or (l2 != None and l2.next != None):
                tmp.next = ListNode()
                tmp = tmp.next

            if l1 != None: l1 = l1.next
            if l2 != None: l2 = l2.next

        if carry != 0: tmp.next = ListNode(carry)
        return head

### TEST CASES

arr1 = [9, 9, 9, 9, 9, 9, 9]
l1 = ListNode()
tmp = l1

for num in arr1:
    tmp.val = num
    if arr1.index(num) != len(arr1) - 1: 
        tmp.next = ListNode()
        tmp = tmp.next

arr2 = [9,9,9,9]
l2 = ListNode()
tmp = l2

for num in arr2:
    tmp.val = num
    if arr2.index(num) != len(arr2) - 1: 
        tmp.next = ListNode()
        tmp = tmp.next

sol = Solution()
head = sol.addTwoNumbers(l1, l2)
while (head != None):
    print(head.val)
    head = head.next

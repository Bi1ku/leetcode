from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        current = l1
        first_num = str(current.val)
        while (current.next != None):
            current = current.next
            first_num += str(current.val)

        current = l2
        second_num = str(current.val)
        while (current.next != None):
            current = current.next
            second_num += str(current.val)

        sum = str(int(first_num[::-1]) + int(second_num[::-1]))[::-1]

        head = ListNode(int(sum[0]))
        current = head
        sum = sum[1:]
        while (sum != ""):
            current.next = ListNode(int(sum[0]))
            current = current.next
            sum = sum[1:]

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

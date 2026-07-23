# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        total1 = 0
        while l1:
            total1 += l1.val * (10 ** i)
            i += 1
            l1 = l1.next
        total2 = 0
        i = 0
        while l2:
            total2 += l2.val * (10 ** i)
            i += 1
            l2 = l2.next
        total = total1 + total2
        head = ListNode(total % 10)
        total = total // 10
        curr = head
        while total > 0:
            curr.next = ListNode(total % 10)
            total = total // 10
            curr = curr.next
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        backwards = self.reverse(slow.next)
        slow.next = None
        while head and backwards:
            next1 = head.next
            next2 = backwards.next
            head.next = backwards
            backwards.next = next1
            head = next1
            backwards = next2


    def reverse(self, head: Optional[ListNode]) -> Optional([ListNode]):
        prev = None
        c = head
        while c:
            n = c.next
            c.next = prev
            prev = c
            c = n
        return prev
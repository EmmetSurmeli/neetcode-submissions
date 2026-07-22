# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        secondHalf = slow.next
        slow.next = None
        secondHalf = self.reverseLink(secondHalf)
        
        c = head
        while secondHalf:
            temp1 = c.next
            temp2 = secondHalf.next
            c.next = secondHalf
            secondHalf.next = temp1
            c = temp1
            secondHalf = temp2
            
    def reverseLink(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        c = head
        while c:
            n = c.next
            c.next = prev
            prev = c
            c = n
        return prev
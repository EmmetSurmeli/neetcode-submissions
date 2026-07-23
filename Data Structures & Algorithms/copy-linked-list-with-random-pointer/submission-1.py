"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        myDict = {}
        curr = head
        while curr:
            myDict[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = myDict[curr]
            copy.next = myDict.get(curr.next)
            copy.random = myDict.get(curr.random)
            curr = curr.next
        return myDict.get(head)
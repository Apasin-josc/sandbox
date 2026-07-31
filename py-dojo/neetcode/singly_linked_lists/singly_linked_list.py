from typing import Optional

""" 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        parts = []
        node = self
        while node:
            parts.append(str(node.val))
            node = node.next
        return " -> ".join(parts) + " -> None"


a, b, c, d = ListNode(0), ListNode(1), ListNode(2), ListNode(3)
a.next = b 
b.next = c
c.next = d
head = a 
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        parts = []
        node = self
        while node:
            parts.append(str(node.val))
            node = node.next
        return " -> ".join(parts) + " -> None"


def build(vals):
    dummy = ListNode()
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next
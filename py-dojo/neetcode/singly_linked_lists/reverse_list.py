from typing import Optional
from singly_linked_list import ListNode, build

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


print(Solution().reverseList(build([0, 1, 2, 3])))

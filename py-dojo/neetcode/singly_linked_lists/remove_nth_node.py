from typing import Optional
from singly_linked_list import ListNode, build

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        N = 0
        while curr:
            N += 1
            curr = curr.next

        removeIndex = N - n
        """
        in the case that head = [1,2,3,4] and n = 4
        removeindex = 4 - 4 = 0
        return head.next = [2,3,4]
        """
        if removeIndex == 0:
            return head.next

        curr = head
        for i in range(N - 1):
            if removeIndex == i + 1:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head

print(Solution().removeNthFromEnd(build([1,2,3,4,5,6,7,8,9]), 2)) 
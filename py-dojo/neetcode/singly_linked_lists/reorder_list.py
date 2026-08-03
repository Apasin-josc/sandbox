from typing import Optional
from singly_linked_list import ListNode, build

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None
        
        while curr:
            nnext = curr.next
            curr.next = prev
            prev = curr
            curr = nnext

        #print(prev) #6 -> 5 -> 4 -> None
        #print(head) #0 -> 1 -> 2 -> 3 -> None

        dummy, current = ListNode(), ListNode()
        dummy.next = current

        while head and prev:
            current.next = head
            head = head.next
            current = current.next

            current.next = prev
            prev = prev.next
            current = current.next

        while head:
            current.next = head
            head = head.next
            current = current.next

        while prev:
            current.next = prev
            prev = prev.next
            current = current.next

        return dummy.next.next


print(Solution().reorderList(build([0,1,2,3,4,5,6,])))
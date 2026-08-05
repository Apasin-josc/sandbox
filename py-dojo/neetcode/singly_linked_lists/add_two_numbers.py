from singly_linked_list import ListNode, build
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        array_l1 = []
        array_l2 = []

        head_l1 = l1
        head_l2 = l2

        while head_l1:
            array_l1.append(head_l1.val)
            head_l1 = head_l1.next

        while head_l2:
            array_l2.append(head_l2.val)
            head_l2 = head_l2.next

        result = []
        carry = 0
        i = 0

        while i < len(array_l1) or i < len(array_l2) or carry:
            d1 = array_l1[i] if i < len(array_l1) else 0
            d2 = array_l2[i] if i < len(array_l2) else 0

            total = d1 + d2 + carry

            digit = total % 10
            carry  = total // 10

            result.append(digit)
            i += 1
            

        dummy = ListNode(0)
        current = dummy
        for v in result:
            current.next = ListNode(v)
            current = current.next
        return dummy.next
        

print(Solution().addTwoNumbers(build([1,2,3]), build([4,5,6])))
print(Solution().addTwoNumbers(build([9]), build([9])))
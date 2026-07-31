from typing import Optional
from singly_linked_list import ListNode, build

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print(list1)
        print(list2)


print(Solution().mergeTwoLists(build([1, 2, 4]), build([1, 3, 5])))
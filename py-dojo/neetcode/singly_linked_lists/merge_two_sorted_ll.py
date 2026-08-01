from typing import Optional
from singly_linked_list import ListNode, build

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy, curr = ListNode(0), ListNode(0)
        dummy.next = curr
        
        
        while list1 and list2:
            
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                
            else:
                curr.next = list2
                list2 = list2.next
        
            curr = curr.next
            
        while list1:
            curr.next = list1
            list1 = list1.next
            curr = curr.next
            
        while list2:
            curr.next = list2
            list2 = list2.next
            curr = curr.next
            
        return dummy.next.next
        

print(Solution().mergeTwoLists(build([1, 2, 4]), build([1, 3, 5])))
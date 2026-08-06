from typing import List
from singly_linked_list import ListNode, build

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return num
            hash_set.add(num)
        return -1
        
print(Solution().findDuplicate([1,2,3,2,2]))
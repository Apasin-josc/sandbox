from typing import List

def hasDuplicateNaive(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    
    return False

"""
T: O(n²)
S: O(1)
"""

def hasDuplicate(nums: List[int]) -> bool:
    seen_numbers = set()
    for num in nums:
        if num in seen_numbers:
            return True
        seen_numbers.add(num)
    return False

"""
T: O(n)
S: O(n)
"""

print(hasDuplicateNaive([1,2,3,3]))
print(hasDuplicate([1,2,3,3]))
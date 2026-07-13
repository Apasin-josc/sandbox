from typing import List
def twoSumNaive(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []

"""
T: O(n²)
S: O(1)
"""



def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums_map:
            return [nums_map[complement], i]
        else:
            nums_map[nums[i]] = i
    return []

"""
T: O(n)
S: O(n)
"""

print(twoSumNaive([3,4,5,6], 7))
print(twoSum([3,4,5,6], 7))
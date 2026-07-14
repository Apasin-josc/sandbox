from typing import List
def topKFrequent(nums: List[int], k: int) -> List[int]:
    nums_map = {}
    for num in nums:
        nums_map[num] = nums_map.get(num, 0) + 1
    
    arr = []

    for key, value in nums_map.items():
        arr.append([key, value])
    
    arr.sort(key=lambda x: x[1])

    ans = []
    for _ in range(k):
        ans.append(arr.pop()[0])

    return ans

print(topKFrequent([1,2,2,3,3,3], 2))

"""
T: O(n.log(n))
S: O(n)
"""
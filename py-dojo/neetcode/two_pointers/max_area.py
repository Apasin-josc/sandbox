from typing import List

def maxArea(heights: List[int]) -> int:
    i, j = 0, len(heights) - 1
    max_area = 0
    
    while i < j:
        
        height = min(heights[i], heights[j])
        area = (j-i) * (height)
        max_area = max(area, max_area)
        
        if heights[i] <= heights[j]:
            i += 1
        else:
            j -=1
    
    return max_area        
        

print(maxArea([1,7,2,5,4,7,3,6]))    


"""
T: O(n)
S: O(1)
"""

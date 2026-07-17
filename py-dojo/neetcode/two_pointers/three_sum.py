from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums_sorted = sorted(nums)
    ans = []
    
    for i in range(len(nums_sorted)):
        #skipping duplicates on i (except the first one)
        if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
            continue
        
        j, k = i + 1, len(nums_sorted) - 1
        
        while j < k:
            triplet = nums_sorted[i] + nums_sorted[j] + nums_sorted[k]
            
            if triplet == 0:
                ans.append([nums_sorted[i], nums_sorted[j], nums_sorted[k]])
                j += 1
                k -= 1
                
                #skipping duplicates on j
                while j < k and nums_sorted[j] == nums_sorted[j-1]:
                    continue
                
                #skipping duplicates on k
                while j < k and nums_sorted[k] == nums_sorted[k+1]:
                    continue
            
            elif triplet > 0:
                k -= 1
            else:
                j += 1
    
    return ans

print(threeSum([-1,0,1,2,-1,-4])) 
#[-4, -1, -1, 0, 1, 2]
#Output: [[-1,-1,2],[-1,0,1]]

"""
Total = O(n²) + O(n log n) = O(n²)
T: O(n²)
S: O(n)
"""

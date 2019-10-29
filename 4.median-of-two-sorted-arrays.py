# @lc app=leetcode id=4 lang=python3
# @lc code=start
def compare(A, B, a, b):
    if A[a] > B[b]:
        if B[b] >= A[a-1]:
            return False
        else:
            return True
    elif B[b] > A[a]:
        if A[a] >= B[b-1]:
            return False
        else:
            return True
    else:
        return False
    
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #find min A, B
        #compare mid min, mid max
            #if mid min > mid max:
                #increase min, decrease max
            #elif mid max > mid min:
                #increase max, decrease min

        
        return 
# @lc code=end


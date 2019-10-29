# @lc app=leetcode id=26 lang=python3
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cursor = None
        idx = 0

        while idx < len(nums):
            if cursor == nums[idx]:
                del nums[idx]
            else:
                cursor = nums[idx]
                idx += 1
        return idx
# @lc code=end


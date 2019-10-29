#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (44.80%)
# Likes:    1609
# Dislikes: 1370
# Total Accepted:    669.8K
# Total Submissions: 1.5M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Example 1:
# 
# 
# Input: 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Follow up:
# 
# Coud you solve it without converting the integer to a string?
# 
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x % 10 == 0 and x >= 10:
            return False

        if x < 10:
            return True
        
        rightSide: int = 0
        while(x > rightSide):
            rightSide = rightSide * 10 + x % 10
            x = x // 10

        return rightSide == x or rightSide // 10 == x



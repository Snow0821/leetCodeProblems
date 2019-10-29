#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.48%)
# Likes:    2417
# Dislikes: 3761
# Total Accepted:    796.7K
# Total Submissions: 3.1M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#
class Solution:
    def reverse(self, x: int) -> int:
        answer = 0
        isNegative = False

        if x < 0:
            isNegative = True
            x = -x
        
        while x >= 10:
            answer = answer*10 + x%10
            x = x//10
        answer = answer*10 + x

        if isNegative:
            answer = -answer

        if answer >= (2**31) or answer < -(2**31):
            answer = 0

        return answer



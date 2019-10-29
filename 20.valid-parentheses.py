# @lc app=leetcode id=20 lang=python3
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        tokens = {'(':')', '{':'}', '[':']'}
        cursor = []
        for c in s:
            if c in tokens:
                cursor.append(c)
                continue
            else:
                if cursor:
                    if c == tokens[cursor.pop()]:
                        continue
                    else:
                        return False
                else:
                    return False
        
        return not cursor
        
# @lc code=end


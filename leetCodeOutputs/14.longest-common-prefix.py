#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.11%)
# Likes:    1596
# Dislikes: 1457
# Total Accepted:    537.5K
# Total Submissions: 1.6M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#


class TrieNode(object):
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.children = {}
        return
    

class Trie(object):
    def __init__(self):
        self.head = TrieNode(None)
        return

    def insert(self, string):
        cursor = self.head
        for c in string:
            if c not in cursor.children:
                cursor.children[c] = TrieNode(c)
            cursor = cursor.children[c]
        cursor.data = string
        return

    def lcp(self):
        cursor = self.head
        lcpString = ""
        while len(cursor.children) == 1:
            if cursor.data != None:
                return cursor.data
            else:
                keyValue = list(cursor.children.keys())[0]
                lcpString += keyValue
                cursor = cursor.children[keyValue]
        return lcpString

    # def search(self, string):
    #     cursor = self.head
    #     for c in string:
    #         if c in cursor.children:
    #             cursor = cursor.children[c]
    #         else:
    #             return False
    #         if cursor.data != None:
    #             return True
    #         else:
    #             print("Error: No cursorData")
    #             return False
    #     return

    # def startsWith(self, prefix):
    #     cursor = self.head
    #     results = []
    #     subTrie = None

    #     for c in prefix:
    #         if c in cursor.children:
    #             cursor = cursor.children[c]
    #             subTrie = cursor
    #         else:
    #             return None

    #     queue = list(subTrie.children.values())

    #     while queue:
    #         cursor_bfs = queue.pop()
    #         if cursor_bfs.data != None:
    #             results.append(cursor_bfs.data)
    #         queue += list(cursor_bfs.children.values())

    #     return results

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        #TRIE SOLUTION
        if len(strs) == 0:
            return ""

        trie = Trie()
        for word in strs:
            if word == "":
                return ""
            trie.insert(word)

        return trie.lcp()


        # DRAFT 1
        # lcp: str = ""
        # strs = sorted(strs, key= len)
        # print(strs)
        # if len(strs) == 0:
        #     return ""
        # for i in range(len(strs[0])):
        #     c = strs[0][i]
        #     for s in strs:
        #         if s[i] != c:
        #             c = ""
        #             break
        #     if c == "":
        #         break
        #     else:
        #         lcp += c
        # return lcp

        # DRAFT 2
        # if len(strs) == 0:
        #     return ""
        # prefix: str = strs[0]
        
        # for i in range(1, len(strs)):
        #     while(strs[i].find(prefix) != 0):
        #         prefix = prefix[:-1]
        #         if len(prefix) == 0:
        #             return ""
        
        # return prefix

        #DRAFT 3
        # if len(strs) == 0:
        #     return ""
        # for i in range(len(strs[0])):
        #     c = strs[0][i]
        #     for j in range(1, len(strs)):
        #         if i == len(strs[j]) or strs[j][i] != c:
        #             return strs[0][:i]
        # return strs[0]

        #DRAFT 4
    #     if len(strs) == 0:
    #         return ""
    #     else:
    #         print("HI")
    #         return self.lcp(strs)

    # def lcp(self, strs: List[str]) -> str:
    #     if len(strs) == 1:
    #         return strs[0]
    #     else:
    #         mid: int = len(strs) // 2
    #         lcpLeft: str = self.lcp(strs[:mid])
    #         lcpRight: str = self.lcp(strs[mid:])
    #         return self.commonPrefix(lcpLeft, lcpRight)

    # def commonPrefix(self, left: str, right: str) -> str:
    #     minimum: int = len(min(left, right, key = len))
    #     for i in range(minimum):
    #         if left[i] != right[i]:
    #             print(left)
    #             return left[:i]
    #     return left


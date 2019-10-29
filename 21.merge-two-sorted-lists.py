# @lc app=leetcode id=21 lang=python3
# @lc code=start

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            if l2 is None:
                return None
            else:
                return l2
        elif l2 is None:
            return l1

        resultHead, l1, l2 = setResultHead(l1, l2)

        resultTail = resultHead
        while True:
            if not l1:
                resultTail.next = l2
                break
            elif not l2:
                resultTail.next = l1
                break
            else:
                if l1.val > l2.val:
                    resultTail.next = l2
                    l2 = l2.next
                else:
                    resultTail.next = l1
                    l1 = l1.next
                resultTail = resultTail.next
                continue
            
        return resultHead

def setResultHead(l1, l2):
    resultHead = None
    if l1.val > l2.val:
        resultHead = l2
        l2 = l2.next

    else:
        resultHead = l1
        l1 = l1.next

    return resultHead, l1, l2
        
# @lc code=end

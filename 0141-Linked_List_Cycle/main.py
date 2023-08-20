from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        iter1 = head
        iter2 = head

        while iter1 and iter2:
            try:
                iter1 = iter1.next
                iter2 = iter2.next.next
            except:
                return False

            if iter1 == iter2:
                return True

        return False
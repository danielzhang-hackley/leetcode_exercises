from typing import Optional
from copy import copy
from time import sleep


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        initial:
        1 -> 2 -> 3 -> 4 -> 5

        partial output:
        5 -> 4 -> 3

        next step: 3.next = 2
        """
        if not (head and head.next):
            return head
        
        cur = prev = self.reverseList(head.next)
        while cur.next:
            cur = cur.next

        head.next = None
        cur.next = head

        return prev
        
solution = Solution()

cur = head = ListNode(1)
for i in [ListNode(2), ListNode(3), ListNode(4), ListNode(5)]:
    cur.next = i
    cur = cur.next

res = solution.reverseList(head)
while res:
    print(res.val)
    res = res.next

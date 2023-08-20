from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
solution = Solution()

cur = head = ListNode(1)
for i in [ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(6)]:
    cur.next = i
    cur = cur.next

res = solution.middleNode(head)
print(res.val)